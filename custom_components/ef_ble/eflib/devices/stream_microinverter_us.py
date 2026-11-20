from ..props import pb_field
from ..props.transforms import pround
from . import stream_microinverter

pb = stream_microinverter.pb


class Device(stream_microinverter.Device):
    """
    STREAM Microinverter (US)

    A separate SKU from the `BK01`/`BK02` microinverter rather than a regional relabel,
    and it carries four PV inputs instead of two. Confirmed against a capture where the
    third and fourth inputs report real power while the first two sit at zero, and where
    inputs two and three share a voltage reading exactly - which is what two sockets wired
    into one MPPT look like on this hardware.
    """

    # `BK06` is the same four-input US unit; confirmed on a live device whose PV3 and
    # PV4 report real power.
    SN_PREFIX = (b"N011", b"BK06")

    pv_power_3 = pb_field(pb.pow_get_pv3, pround(2))
    pv_voltage_3 = pb_field(pb.plug_in_info_pv3_vol, pround(1))
    pv_current_3 = pb_field(pb.plug_in_info_pv3_amp, pround(2))

    pv_power_4 = pb_field(pb.pow_get_pv4, pround(2))
    pv_voltage_4 = pb_field(pb.plug_in_info_pv4_vol, pround(1))
    pv_current_4 = pb_field(pb.plug_in_info_pv4_amp, pround(2))
