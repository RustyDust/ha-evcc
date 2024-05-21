from typing import Final

JSONKEY_PLANS: Final = "plans"
JSONKEY_PLANS_SOC: Final = "soc"
JSONKEY_PLANS_TIME: Final = "time"

JSONKEY_LOADPOINTS: Final = "loadpoints"
JSONKEY_VEHICLES: Final = "vehicles"
JSONKEY_AUXPOWER: Final = "auxPower"
JSONKEY_BATTERYMODE: Final = "batteryMode"
JSONKEY_BATTERYPOWER: Final = "batteryPower"
JSONKEY_BATTERYSOC: Final = "batterySoc"
JSONKEY_GRIDCURRENTS: Final = "gridCurrents"
JSONKEY_GRIDPOWER: Final = "gridPower"
JSONKEY_HOMEPOWER: Final = "homePower"
JSONKEY_PVPOWER: Final = "pvPower"

STATES: Final = [JSONKEY_LOADPOINTS, JSONKEY_VEHICLES, JSONKEY_AUXPOWER, JSONKEY_BATTERYMODE, JSONKEY_BATTERYPOWER,
                 JSONKEY_BATTERYSOC, JSONKEY_GRIDCURRENTS, JSONKEY_GRIDPOWER, JSONKEY_HOMEPOWER, JSONKEY_PVPOWER]

FILTER_LOADPOINTS: Final = f"?jq=.{JSONKEY_LOADPOINTS}"
STATE_QUERY = (
    f"?jq={{{JSONKEY_AUXPOWER}:.{JSONKEY_AUXPOWER},{JSONKEY_BATTERYMODE}:.{JSONKEY_BATTERYMODE},{JSONKEY_BATTERYPOWER}:.{JSONKEY_BATTERYPOWER},{JSONKEY_BATTERYSOC}:.{JSONKEY_BATTERYSOC},{JSONKEY_GRIDCURRENTS}:.{JSONKEY_GRIDCURRENTS},{JSONKEY_GRIDPOWER}:.{JSONKEY_GRIDPOWER},{JSONKEY_HOMEPOWER}:.{JSONKEY_HOMEPOWER},{JSONKEY_HOMEPOWER}:.{JSONKEY_HOMEPOWER},{JSONKEY_PVPOWER}:.{JSONKEY_PVPOWER},{JSONKEY_VEHICLES}:.{JSONKEY_VEHICLES}}}"
)

MIN_CURRENT_LIST: Final = ["0.125", "0.25", "0.5", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                           "14", "15", "16"]

MAX_CURRENT_LIST: Final = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                           "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]

BATTERY_LIST: Final = ["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75",
                       "80", "85", "90", "95", "100"]

TRANSLATIONS: Final = {
    "de": {
        "batterymode": {
            "unknown": "Unbekannt",
            "normal": "normal",
            "hold": "angehalten/gesperrt",
            "charge": "laden...",
        },
        "phaseaction":{
            "scale1p": "Reduziere auf einphasig",
            "scale3p": "Erhöhe auf dreiphasig",
            "inactive": "-kein-"
        }
    },
    "en": {
        "batterymode": {
            "unknown": "unknown",
            "normal": "normal",
            "hold": "on-hold",
            "charge": "charging...",
        },
        "phaseaction":{
            "scale1p": "Reducing to 1-phase charging",
            "scale3p": "Increasing to 3-phase charging",
            "inactive": "-none-"
        }
    }
}
