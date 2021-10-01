from datetime import datetime

from lib_bgp_simulator.engine.bgp_as import BGPAS
from lib_bgp_simulator.engine.simulator_engine import SimulatorEngine


# tmp_path is a pytest fixture
def run_example(peers=list(),
                customer_providers=list(),
                as_policies=dict(),
                announcements=list(),
                local_ribs=dict(),
                BaseASCls=BGPAS,
                ):
    """Runs an example"""

    print("populating engine")
    start = datetime.now()
    engine = SimulatorEngine(set(customer_providers),
                             set(peers),
                             BaseASCls=BaseASCls)
    for asn, as_policy in as_policies.items():
        engine.as_dict[asn].policy = as_policy()
    print((start-datetime.now()).total_seconds())
    print("Running engine")
    start = datetime.now()
    engine.run(announcements)
    print((start-datetime.now()).total_seconds())
    if local_ribs:
        for as_obj in engine:
            print("ASN:", as_obj.asn)
            for prefix, ann in as_obj.policy.local_rib.items():
                print(ann)
            as_obj.policy.local_rib.assert_eq(local_ribs[as_obj.asn])
