Core Engine API
===============

The RAFAEL Core Engine is the heart of the framework, managing the Adaptive Resilience Genome (ARG)
and coordinating evolution.

RafaelCore
----------

.. autoclass:: core.rafael_engine.RafaelCore
   :members:
   :undoc-members:
   :show-inheritance:

Adaptive Resilience Genome
---------------------------

.. autoclass:: core.rafael_engine.AdaptiveResilienceGenome
   :members:
   :undoc-members:
   :show-inheritance:

Gene
----

.. autoclass:: core.rafael_engine.Gene
   :members:
   :undoc-members:
   :show-inheritance:

Mutation Orchestrator
---------------------

.. autoclass:: core.rafael_engine.MutationOrchestrator
   :members:
   :undoc-members:
   :show-inheritance:

Fitness Evaluator
-----------------

.. autoclass:: core.rafael_engine.FitnessEvaluator
   :members:
   :undoc-members:
   :show-inheritance:

Enums
-----

ResilienceStrategy
~~~~~~~~~~~~~~~~~~

.. autoclass:: core.rafael_engine.ResilienceStrategy
   :members:
   :undoc-members:

IsolationLevel
~~~~~~~~~~~~~~

.. autoclass:: core.rafael_engine.IsolationLevel
   :members:
   :undoc-members:

Examples
--------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from core.rafael_engine import RafaelCore, ResilienceStrategy
   
   # Initialize core
   core = RafaelCore(
       app_name="my-application",
       resilience_level="adaptive"
   )
   
   # Register module with specific strategies
   genome = core.register_module(
       "api_module",
       initial_strategies=[
           ResilienceStrategy.RETRY_ADAPTIVE,
           ResilienceStrategy.CIRCUIT_BREAKER,
           ResilienceStrategy.TIMEOUT
       ]
   )
   
   print(f"Module registered with {len(genome.genes)} genes")

Evolution
~~~~~~~~~

.. code-block:: python

   import asyncio
   
   async def evolve_system():
       core = RafaelCore(app_name="evolving-app")
       core.register_module("critical_module")
       
       # Trigger single evolution
       result = await core.evolve_module("critical_module")
       print(f"Fitness score: {result.fitness_score}")
       
       # Start autonomous evolution
       await core.start_evolution(interval_seconds=3600)
       
       # Let it run...
       await asyncio.sleep(7200)
       
       # Stop evolution
       core.stop_evolution()
   
   asyncio.run(evolve_system())

Reporting
~~~~~~~~~

.. code-block:: python

   # Get comprehensive resilience report
   report = core.get_resilience_report()
   
   print(f"Application: {report['app_name']}")
   print(f"Modules: {len(report['modules'])}")
   
   for module_id, info in report['modules'].items():
       print(f"\nModule: {module_id}")
       print(f"  Generation: {info['generation']}")
       print(f"  Genes: {info['genes_count']}")
       print(f"  Avg Fitness: {info['avg_fitness']:.2f}")
       
       print("  Best Genes:")
       for gene in info['best_genes']:
           print(f"    - {gene['strategy']}: {gene['fitness']:.2f}")

Export/Import
~~~~~~~~~~~~~

.. code-block:: python

   # Export genome for sharing
   genome_json = core.export_genome("my_module")
   
   # Save to file
   with open("genome_backup.json", "w") as f:
       f.write(genome_json)
   
   # Later, import it
   with open("genome_backup.json", "r") as f:
       genome_data = f.read()
   
   # Apply to new module
   # (Implementation depends on your use case)
