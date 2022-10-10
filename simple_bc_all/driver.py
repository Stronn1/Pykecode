import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)
    
def bc_test_questions():

    engine.reset()      

    engine.activate('rules') 
    
    try:
        with engine.prove_goal('rules.especie($esp)') as gen: 
            for vars, plan in gen:
                print("Especie: %s" % (vars['esp'])) 

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


