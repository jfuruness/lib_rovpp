from datetime import datetime
from pathlib import Path

from lib_bgp_simulator import Graph, Simulator, ROVAS, MPMethod

# LITE
from .as_classes import ROVPPV1LiteSimpleAS
from .as_classes import ROVPPV2LiteSimpleAS
from .as_classes import ROVPPV2aLiteSimpleAS

# NON LITE
from .as_classes import ROVPPV1SimpleAS
from .as_classes import ROVPPV2SimpleAS
from .as_classes import ROVPPV2aSimpleAS
from .as_classes import ROVPPV3AS

# Attacks
from .engine_input import ROVPPSubprefixHijack
from .engine_input import ROVPPNonRoutedSuperprefixHijack
from .engine_input import ROVPPSuperprefixPrefixHijack
from .engine_input import ROVPPPrefixHijack


default_kwargs = {"percent_adoptions": [0, 5, 10, 20, 30, 40, 60, 80, 100],
                  "num_trials": 5}

non_lite_policies =(ROVPPV1SimpleAS,
                    ROVPPV2SimpleAS,
                    ROVPPV2aSimpleAS,
                    ROVPPV3AS)

rov_non_lite_rovpp = (ROVAS,) + non_lite_policies


def run_sim(graph, path):
    sim = Simulator(parse_cpus=6)

    sim.run(graphs=[graph], graph_path=path, mp_method=MPMethod.MP)


def main():

    assert isinstance(input("Turn asserts off for speed?"), str)

    # Get's all of the general graphs for all types of attacks
    for atk in [ROVPPSubprefixHijack,
                ROVPPNonRoutedSuperprefixHijack,
                ROVPPSuperprefixPrefixHijack,
                ROVPPPrefixHijack]:
        kwargs = {"EngineInputCls": atk, **default_kwargs}
        graph = Graph(adopt_as_classes=rov_non_lite_rovpp, **kwargs)

        run_sim(graph, Path(f"/home/anon/{atk.__name__}_graphs.tar.gz"))
        print(f"Completed {atk}")

    kwargs = {"EngineInputCls": ROVPPSubprefixHijack, **default_kwargs}
    graph = Graph(adopt_as_classes=[ROVPPV1LiteSimpleAS, ROVPPV1SimpleAS],
                  **kwargs)
    run_sim(graph, Path("/home/anon/v1_lite_vs_non_lite_graphs.tar.gz"))

if __name__ == "__main__":
    start = datetime.now()
    main()
    print((datetime.now() - start).total_seconds())
