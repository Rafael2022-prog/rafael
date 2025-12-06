"""
RAFAEL Framework - Web Dashboard
Modern web interface for monitoring and managing RAFAEL systems
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core import RafaelCore, AdaptiveResilienceGenome
from chaos_forge import ChaosForge, ThreatType
from vault import ResilienceVault
from guardian import GuardianLayer

app = Flask(__name__)
CORS(app)

# Initialize RAFAEL components
rafael = RafaelCore(app_name="rafael-dashboard")
chaos_forge = ChaosForge()
vault = ResilienceVault()
guardian = GuardianLayer()

# Sample data for demo
demo_modules = ["payment-service", "auth-service", "notification-service"]
for module in demo_modules:
    rafael.register_module(module)

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """Get overall system status"""
    modules = []
    for module_id in demo_modules:
        genome = rafael.genomes.get(module_id)
        if genome:
            modules.append({
                'id': module_id,
                'fitness': genome.fitness_score,
                'generation': genome.generation,
                'genes_count': len(genome.genes),
                'status': 'healthy' if genome.fitness_score > 0.7 else 'warning' if genome.fitness_score > 0.4 else 'critical'
            })
    
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'total_modules': len(demo_modules),
        'healthy_modules': sum(1 for m in modules if m['status'] == 'healthy'),
        'modules': modules,
        'vault_patterns': len(vault.patterns),
        'pending_approvals': len(guardian.pending_approvals)
    })

@app.route('/api/modules')
def get_modules():
    """Get all registered modules"""
    modules = []
    for module_id in demo_modules:
        genome = rafael.genomes.get(module_id)
        if genome:
            modules.append({
                'id': module_id,
                'fitness': genome.fitness_score,
                'generation': genome.generation,
                'genes': [
                    {
                        'strategy': gene.strategy.value,
                        'params': gene.parameters,
                        'fitness': gene.fitness_score
                    } for gene in genome.genes
                ]
            })
    
    return jsonify({'modules': modules})

@app.route('/api/modules/<module_id>/evolve', methods=['POST'])
def evolve_module(module_id):
    """Trigger evolution for a module"""
    try:
        rafael.evolve_module(module_id)
        genome = rafael.genomes.get(module_id)
        
        return jsonify({
            'success': True,
            'module_id': module_id,
            'new_fitness': genome.fitness_score,
            'generation': genome.generation
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/chaos/simulate', methods=['POST'])
def simulate_chaos():
    """Run chaos simulation"""
    data = request.json
    module_id = data.get('module_id', demo_modules[0])
    threat_type = data.get('threat_type', 'ddos')
    
    try:
        # Get threat type enum
        threat = ThreatType[threat_type.upper()]
        
        # Run simulation
        result = chaos_forge.simulate_attack(
            module_id=module_id,
            threat_type=threat,
            duration_seconds=10
        )
        
        return jsonify({
            'success': True,
            'result': {
                'module_id': result.module_id,
                'threat_type': result.threat_type.value,
                'severity': result.severity.value,
                'success_rate': result.success_rate,
                'resilience_score': result.resilience_score,
                'recommendations': result.recommendations
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/vault/patterns')
def get_patterns():
    """Get all resilience patterns"""
    patterns = []
    for pattern in vault.patterns.values():
        patterns.append({
            'id': pattern.pattern_id,
            'name': pattern.name,
            'category': pattern.category.value,
            'description': pattern.description,
            'effectiveness': pattern.effectiveness_score,
            'use_count': pattern.use_count
        })
    
    return jsonify({'patterns': patterns})

@app.route('/api/vault/search', methods=['POST'])
def search_patterns():
    """Search patterns by criteria"""
    data = request.json
    tech = data.get('tech')
    category = data.get('category')
    
    results = vault.search_patterns(
        technology=tech,
        category=category
    )
    
    patterns = []
    for pattern in results:
        patterns.append({
            'id': pattern.pattern_id,
            'name': pattern.name,
            'category': pattern.category.value,
            'description': pattern.description,
            'effectiveness': pattern.effectiveness_score
        })
    
    return jsonify({'patterns': patterns})

@app.route('/api/guardian/approvals')
def get_approvals():
    """Get pending approvals"""
    approvals = []
    for approval_id, request in guardian.pending_approvals.items():
        approvals.append({
            'id': approval_id,
            'module_id': request.module_id,
            'change_type': request.change.change_type,
            'timestamp': request.timestamp.isoformat(),
            'impact': request.impact.value if request.impact else 'unknown'
        })
    
    return jsonify({'approvals': approvals})

@app.route('/api/guardian/approve/<approval_id>', methods=['POST'])
def approve_change(approval_id):
    """Approve a pending change"""
    data = request.json
    approver = data.get('approver', 'admin')
    
    try:
        guardian.approve_change(approval_id, approver)
        return jsonify({'success': True, 'approval_id': approval_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/guardian/reject/<approval_id>', methods=['POST'])
def reject_change(approval_id):
    """Reject a pending change"""
    data = request.json
    approver = data.get('approver', 'admin')
    reason = data.get('reason', 'No reason provided')
    
    try:
        guardian.reject_change(approval_id, approver, reason)
        return jsonify({'success': True, 'approval_id': approval_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/stats')
def get_stats():
    """Get system statistics"""
    total_genes = sum(len(g.genes) for g in rafael.genomes.values())
    avg_fitness = sum(g.fitness_score for g in rafael.genomes.values()) / len(rafael.genomes) if rafael.genomes else 0
    
    return jsonify({
        'total_modules': len(rafael.genomes),
        'total_genes': total_genes,
        'average_fitness': round(avg_fitness, 3),
        'vault_patterns': len(vault.patterns),
        'pending_approvals': len(guardian.pending_approvals),
        'audit_logs': len(guardian.audit_log)
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🔱 RAFAEL Dashboard starting...")
    print("📊 Dashboard URL: http://localhost:5000")
    print("🚀 API Docs: http://localhost:5000/api/status")
    app.run(host='0.0.0.0', port=5000, debug=True)
