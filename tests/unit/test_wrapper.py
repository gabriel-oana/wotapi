import os
import unittest
from wotapi.models.models import REALM
from wotapi.orm.data_model import DataModel
from wotapi.helper.db_loader import DBLoader
from wotapi.helper.create_engine import create_db_engine


class TestWrapper(unittest.TestCase):

    def setUp(self) -> None:
        self.test_account_id = 'mock_account_id'
        self.test_application_id = 'mock_application_id'
        self.test_token = 'mock_token'
        self.test_realm = REALM.eu

        self.db_path = f'tests'
        self.engine = create_db_engine(path=self.db_path)
        self.db_loader = DBLoader(db_engine=self.engine)
        DataModel.create_tables(engine=self.engine)

    @staticmethod
    def mock_renew_access_token(account_id: str) -> dict:
        response = {"status": "ok", "meta": {"count": 3},
                    "data": {"access_token": "49a5800faeb33fcc49adb62dfbccc912b8694cec", "account_id": account_id,
                             "expires_at": 1666035021}}
        return response

    @staticmethod
    def mock_account_id() -> dict:
        response = {"status": "ok", "meta": {"count": 1}, "data": [{"nickname": "mock-nickname", "account_id": 1}]}
        return response

    @staticmethod
    def mock_response_player_achievements(account_id: str) -> dict:
        response = {
            "status": "ok",
            "meta": {"count": 1},
            "data": {
                account_id: {
                    "achievements": {
                        "medalCarius": 1,
                    },
                    "frags": {
                        "crucialShotMedal": 3
                    },
                    "max_series": {
                        "armorPiercer": 23
                    }
                }
            }
        }

        return response

    @staticmethod
    def mock_response_player_personal(account_id: str):
        response = {"status": "ok", "meta": {"count": 1}, "data": {
            account_id: {"client_language": "", "last_battle_time": 1648900023, "account_id": 508670392,
                         "created_at": 1361579208, "updated_at": 1658457031,
                         "private": {"restrictions": {"chat_ban_time": None}, "gold": 5243, "free_xp": 14339,
                                     "ban_time": None, "is_bound_to_phone": True, "is_premium": False,
                                     "credits": 7761405, "premium_expires_at": 1557394809, "bonds": 2049,
                                     "battle_life_time": 6239005, "ban_info": None}, "global_rating": 6187,
                         "clan_id": 500136157, "statistics": {
                    "clan": {"spotted": 0, "battles_on_stunning_vehicles": 0, "avg_damage_blocked": 0.0,
                             "direct_hits_received": 0, "explosion_hits": 0, "piercings_received": 0, "piercings": 0,
                             "xp": 0, "survived_battles": 0, "dropped_capture_points": 0, "hits_percents": 0,
                             "draws": 0, "battles": 0, "damage_received": 0, "avg_damage_assisted": 0.0,
                             "avg_damage_assisted_track": 0.0, "frags": 0, "stun_number": 0,
                             "avg_damage_assisted_radio": 0.0, "capture_points": 0, "stun_assisted_damage": 0,
                             "hits": 0, "battle_avg_xp": 0, "wins": 0, "losses": 0, "damage_dealt": 0,
                             "no_damage_direct_hits_received": 0, "shots": 0, "explosion_hits_received": 0,
                             "tanking_factor": 0.0},
                    "all": {"spotted": 18600, "battles_on_stunning_vehicles": 254, "max_xp": 2316,
                            "avg_damage_blocked": 406.24, "direct_hits_received": 94110, "explosion_hits": 4357,
                            "piercings_received": 65748, "piercings": 80139, "max_damage_tank_id": 12049,
                            "xp": 12150715, "survived_battles": 5699, "dropped_capture_points": 15075,
                            "hits_percents": 66, "draws": 199, "max_xp_tank_id": 54017, "battles": 21896,
                            "damage_received": 20668629, "avg_damage_assisted": 340.53, "max_frags_tank_id": 8993,
                            "avg_damage_assisted_track": 83.72, "frags": 19578, "stun_number": 1449,
                            "avg_damage_assisted_radio": 256.81, "capture_points": 19319,
                            "stun_assisted_damage": 164348, "max_damage": 6776, "hits": 130296, "battle_avg_xp": 555,
                            "wins": 11079, "losses": 10618, "damage_dealt": 24841152,
                            "no_damage_direct_hits_received": 27153, "max_frags": 9, "shots": 196463,
                            "explosion_hits_received": 5884, "tanking_factor": 0.39},
                    "regular_team": {"spotted": 0, "battles_on_stunning_vehicles": 0, "max_xp": 0,
                                     "avg_damage_blocked": 0.0, "direct_hits_received": 0, "explosion_hits": 0,
                                     "piercings_received": 0, "piercings": 0, "max_damage_tank_id": None, "xp": 0,
                                     "survived_battles": 0, "dropped_capture_points": 0, "hits_percents": 0, "draws": 0,
                                     "max_xp_tank_id": None, "battles": 0, "damage_received": 0,
                                     "avg_damage_assisted": 0.0, "max_frags_tank_id": None,
                                     "avg_damage_assisted_track": 0.0, "frags": 0, "stun_number": 0,
                                     "avg_damage_assisted_radio": 0.0, "capture_points": 0, "stun_assisted_damage": 0,
                                     "max_damage": 0, "hits": 0, "battle_avg_xp": 0, "wins": 0, "losses": 0,
                                     "damage_dealt": 0, "no_damage_direct_hits_received": 0, "max_frags": 0, "shots": 0,
                                     "explosion_hits_received": 0, "tanking_factor": 0.0}, "trees_cut": 20353,
                    "company": {"spotted": 0, "battles_on_stunning_vehicles": 0, "avg_damage_blocked": 0.0,
                                "direct_hits_received": 0, "explosion_hits": 0, "piercings_received": 0, "piercings": 0,
                                "xp": 228, "survived_battles": 0, "dropped_capture_points": 0, "hits_percents": 50,
                                "draws": 0, "battles": 1, "damage_received": 460, "avg_damage_assisted": 0.0,
                                "avg_damage_assisted_track": 0.0, "frags": 1, "stun_number": 0,
                                "avg_damage_assisted_radio": 0.0, "capture_points": 0, "stun_assisted_damage": 0,
                                "hits": 5, "battle_avg_xp": 228, "wins": 0, "losses": 1, "damage_dealt": 713,
                                "no_damage_direct_hits_received": 0, "shots": 10, "explosion_hits_received": 0,
                                "tanking_factor": 0.0},
                    "stronghold_skirmish": {"spotted": 0, "battles_on_stunning_vehicles": 0, "max_xp": 0,
                                            "direct_hits_received": 0, "explosion_hits": 0, "piercings_received": 0,
                                            "piercings": 0, "xp": 0, "survived_battles": 0, "dropped_capture_points": 0,
                                            "hits_percents": 0, "draws": 0, "max_xp_tank_id": None, "battles": 0,
                                            "damage_received": 0, "max_frags_tank_id": None, "frags": 0,
                                            "stun_number": 0, "capture_points": 0, "stun_assisted_damage": 0,
                                            "max_damage_tank_id": None, "max_damage": 0, "hits": 0, "battle_avg_xp": 0,
                                            "wins": 0, "losses": 0, "damage_dealt": 0,
                                            "no_damage_direct_hits_received": 0, "max_frags": 0, "shots": 0,
                                            "explosion_hits_received": 0, "tanking_factor": 0.0},
                    "stronghold_defense": {"spotted": 0, "battles_on_stunning_vehicles": 0, "max_xp": 0,
                                           "direct_hits_received": 0, "explosion_hits": 0, "piercings_received": 0,
                                           "piercings": 0, "xp": 0, "survived_battles": 0, "dropped_capture_points": 0,
                                           "hits_percents": 0, "draws": 0, "max_xp_tank_id": None, "battles": 0,
                                           "damage_received": 0, "max_frags_tank_id": None, "frags": 0,
                                           "stun_number": 0, "capture_points": 0, "stun_assisted_damage": 0,
                                           "max_damage_tank_id": None, "max_damage": 0, "hits": 0, "battle_avg_xp": 0,
                                           "wins": 0, "losses": 0, "damage_dealt": 0,
                                           "no_damage_direct_hits_received": 0, "max_frags": 0, "shots": 0,
                                           "explosion_hits_received": 0, "tanking_factor": 0.0},
                    "historical": {"spotted": 0, "battles_on_stunning_vehicles": 0, "max_xp": 886,
                                   "avg_damage_blocked": 60.0, "direct_hits_received": 9, "explosion_hits": 3,
                                   "piercings_received": 8, "piercings": 29, "max_damage_tank_id": 7201, "xp": 2056,
                                   "survived_battles": 2, "dropped_capture_points": 0, "hits_percents": 87, "draws": 0,
                                   "max_xp_tank_id": 1057, "battles": 4, "damage_received": 1189,
                                   "avg_damage_assisted": 382.25, "max_frags_tank_id": 1057,
                                   "avg_damage_assisted_track": 244.0, "frags": 4, "stun_number": 0,
                                   "avg_damage_assisted_radio": 138.25, "capture_points": 0, "stun_assisted_damage": 0,
                                   "max_damage": 1011, "hits": 34, "battle_avg_xp": 514, "wins": 2, "losses": 2,
                                   "damage_dealt": 3643, "no_damage_direct_hits_received": 1, "max_frags": 2,
                                   "shots": 39, "explosion_hits_received": 0, "tanking_factor": 0.18},
                    "team": {"spotted": 59, "battles_on_stunning_vehicles": 0, "max_xp": 1384,
                             "avg_damage_blocked": 314.26, "direct_hits_received": 247, "explosion_hits": 0,
                             "piercings_received": 204, "piercings": 177, "max_damage_tank_id": 3137, "xp": 20870,
                             "survived_battles": 17, "dropped_capture_points": 7, "hits_percents": 78, "draws": 0,
                             "max_xp_tank_id": 5921, "battles": 52, "damage_received": 54056,
                             "avg_damage_assisted": 193.92, "max_frags_tank_id": 7425,
                             "avg_damage_assisted_track": 63.98, "frags": 26, "stun_number": 0,
                             "avg_damage_assisted_radio": 129.94, "capture_points": 26, "stun_assisted_damage": 0,
                             "max_damage": 3284, "hits": 229, "battle_avg_xp": 401, "wins": 19, "losses": 33,
                             "damage_dealt": 50293, "no_damage_direct_hits_received": 43, "max_frags": 3, "shots": 295,
                             "explosion_hits_received": 0, "tanking_factor": 0.24},
                    "frags": {"18497": 20, "3921": 72, "19713": 31, "14913": 1, "59729": 6, "14673": 39, "57681": 2,
                              "44289": 14, "52865": 3, "6721": 46, "54609": 1, "10513": 50, "13089": 47, "55297": 58,
                              "4145": 16, "11265": 102, "5985": 1, "3857": 142, "62785": 9, "53249": 22, "11857": 39,
                              "16673": 57, "14353": 12, "15617": 9, "1793": 29, "58705": 1, "54289": 149, "57937": 5,
                              "4737": 18, "6657": 72, "47121": 4, "4961": 33, "1665": 27, "3681": 30, "21537": 1,
                              "18177": 49, "1121": 30, "46097": 1, "1089": 17, "4657": 77, "273": 73, "16705": 4,
                              "59473": 3, "15105": 14, "57617": 18, "17985": 11, "52097": 53, "7953": 90, "17953": 79,
                              "1409": 11, "53121": 7, "52305": 4, "8737": 28, "529": 229, "13905": 28, "3585": 101,
                              "2449": 7, "4193": 33, "50193": 151, "9489": 76, "16401": 98, "17425": 7, "4353": 124,
                              "33": 8, "55121": 1, "11009": 67, "2049": 45, "641": 1, "49169": 1, "9553": 48,
                              "2161": 55, "4625": 26, "45841": 3, "58913": 10, "20481": 13, "11345": 18, "47361": 10,
                              "17729": 3, "8465": 49, "5137": 239, "48641": 33, "52737": 2, "46865": 9, "8193": 61,
                              "6433": 17, "3457": 6, "12561": 49, "2833": 13, "51345": 1, "57377": 18, "5425": 6,
                              "6209": 39, "14625": 59, "61249": 4, "18209": 73, "44545": 2, "3633": 53, "9745": 134,
                              "14145": 105, "48145": 3, "10241": 21, "5953": 6, "56577": 7, "3201": 3, "5185": 57,
                              "18689": 24, "11537": 94, "12545": 32, "19457": 6, "51489": 4, "60945": 27, "3969": 16,
                              "56657": 17, "2865": 43, "18705": 9, "21025": 6, "52353": 2, "2913": 6, "2945": 2,
                              "62241": 2, "1057": 83, "20257": 2, "3345": 26, "1": 109, "1697": 15, "5921": 39,
                              "10833": 10, "19985": 3, "6977": 52, "145": 5, "15441": 1, "64017": 6, "58881": 2,
                              "12881": 3, "16449": 9, "1889": 34, "17665": 15, "8241": 3, "12289": 18, "61969": 3,
                              "17153": 8, "2129": 65, "2081": 10, "4913": 32, "31233": 11, "62017": 18, "56097": 5,
                              "7185": 79, "10065": 28, "6913": 46, "2657": 36, "61697": 1, "64065": 39, "60689": 7,
                              "8017": 15, "4225": 40, "5457": 57, "17169": 3, "7457": 86, "7969": 54, "20737": 14,
                              "16961": 3, "63793": 4, "60449": 9, "15361": 4, "4385": 108, "55057": 1, "7697": 74,
                              "8497": 2, "1377": 39, "2401": 1, "4865": 15, "11025": 72, "58961": 2, "3937": 8,
                              "10529": 115, "63537": 3, "52817": 1, "20513": 3, "18961": 32, "3841": 7, "22273": 3,
                              "5697": 84, "13393": 4, "20993": 13, "8977": 114, "32769": 1, "5665": 14, "19201": 15,
                              "3889": 53, "60225": 22, "58369": 11, "62753": 1, "81": 12, "22017": 26, "21505": 51,
                              "63233": 1, "7729": 4, "2305": 80, "5969": 56, "18241": 20, "25617": 2, "11281": 25,
                              "16145": 61, "3665": 10, "7681": 10, "16897": 78, "8209": 77, "15953": 6, "3745": 4,
                              "1137": 12, "3153": 44, "14337": 7, "11089": 12, "1633": 26, "19969": 31, "15137": 33,
                              "3393": 8, "20225": 20, "2577": 57, "5409": 46, "51105": 8, "8721": 38, "513": 267,
                              "9249": 31, "11041": 114, "625": 2, "2593": 120, "1345": 2, "56913": 12, "6929": 11,
                              "4433": 71, "51537": 5, "13329": 24, "4945": 5, "7713": 28, "2881": 22, "3697": 6,
                              "57105": 33, "21281": 2, "3089": 16, "7985": 4, "2113": 13, "63281": 34, "2625": 70,
                              "3873": 182, "47377": 6, "10017": 44, "9233": 24, "6401": 16, "54801": 4, "61713": 6,
                              "3441": 7, "7217": 2, "57361": 13, "7761": 19, "10497": 78, "3905": 60, "881": 4,
                              "10273": 48, "61473": 5, "15873": 11, "56145": 1, "14401": 35, "14097": 39, "5217": 28,
                              "57889": 11, "11521": 185, "22529": 8, "53505": 4, "10577": 1, "49409": 2, "3233": 1,
                              "51713": 23, "4161": 15, "53585": 5, "62481": 13, "58193": 1, "19009": 12, "817": 35,
                              "321": 12, "19745": 7, "51089": 13, "16209": 1, "17937": 5, "3985": 1, "12049": 61,
                              "59137": 8, "2977": 3, "43553": 16, "1041": 155, "11793": 59, "609": 5, "5937": 3,
                              "55569": 65, "6961": 2, "8257": 2, "15905": 4, "3713": 8, "52065": 13, "17473": 57,
                              "2097": 35, "5505": 9, "8785": 52, "13569": 33, "15681": 36, "3121": 54, "4673": 31,
                              "20241": 9, "545": 22, "2385": 17, "48385": 7, "56081": 1, "13841": 55, "2465": 32,
                              "64273": 18, "1313": 28, "2705": 15, "4881": 29, "50961": 27, "15425": 8, "20769": 1,
                              "3409": 6, "129": 1, "9985": 30, "51569": 5, "7441": 49, "14161": 17, "1825": 7,
                              "4401": 18, "13313": 30, "929": 4, "2145": 13, "2417": 41, "53761": 4, "10753": 51,
                              "2065": 17, "5393": 51, "14113": 22, "11809": 1, "58657": 3, "5713": 59, "19473": 5,
                              "65073": 1, "1921": 24, "63505": 3, "8449": 27, "833": 3, "4129": 32, "51361": 148,
                              "3473": 15, "3425": 22, "7249": 31, "4497": 1, "61729": 8, "54529": 2, "369": 1,
                              "8961": 20, "5681": 6, "16385": 7, "55889": 14, "15633": 19, "16129": 19, "16657": 150,
                              "22785": 17, "19217": 37, "15889": 38, "53537": 5, "6673": 50, "14609": 62, "6177": 25,
                              "785": 5, "5249": 12, "1809": 127, "1649": 18, "1617": 7, "13137": 15, "32257": 1,
                              "55633": 45, "51745": 4, "11297": 103, "54785": 32, "59905": 59, "15121": 4, "3617": 21,
                              "577": 4, "18193": 158, "60481": 11, "51985": 7, "15649": 68, "3169": 2, "51825": 8,
                              "257": 74, "16161": 57, "14657": 6, "2561": 141, "2209": 40, "3361": 83, "1585": 20,
                              "56353": 14, "11585": 31, "52241": 2, "2369": 10, "56609": 7, "43521": 17, "52321": 10,
                              "63041": 29, "49665": 14, "865": 1, "44033": 2, "9505": 96, "59425": 3, "60417": 19,
                              "15393": 60, "4449": 3, "6481": 76, "7489": 47, "47105": 5, "2897": 98, "4689": 63,
                              "45569": 20, "1105": 143, "60433": 2, "35105": 1, "58113": 48, "10001": 40, "45313": 19,
                              "46849": 4, "12817": 3, "5889": 79, "60465": 4, "1537": 105, "5729": 19, "14881": 47,
                              "7201": 43, "51553": 10, "3185": 11, "61761": 9, "6225": 6, "10769": 100, "7473": 3,
                              "14865": 91, "19729": 27, "60993": 2, "61505": 29, "19489": 1, "5201": 3, "11553": 229,
                              "9761": 26, "45057": 50, "62001": 2, "9041": 41, "673": 2, "13073": 17, "9297": 42,
                              "1601": 1, "62497": 40, "48129": 1, "64817": 39, "7505": 32, "18433": 33, "353": 2,
                              "3105": 48, "13889": 10, "801": 110, "11841": 26, "15169": 1, "61217": 1, "769": 20,
                              "2961": 35, "53793": 1, "2849": 217, "61985": 17, "59649": 8, "5473": 31, "3329": 10,
                              "54353": 14, "49937": 4, "4705": 3, "6193": 15, "54657": 3, "5377": 425, "1073": 25,
                              "289": 23, "10817": 25, "5905": 6, "337": 9, "43585": 18, "8225": 45, "65329": 5,
                              "64561": 24, "1153": 5, "6993": 13, "55073": 3, "3137": 103, "3649": 98, "59393": 7,
                              "6417": 80, "1553": 99, "34081": 3, "4641": 20, "15697": 32, "18449": 42, "60193": 1,
                              "2193": 3, "8705": 22, "54017": 8, "31745": 5, "3601": 9, "11777": 327, "10049": 23,
                              "13857": 25, "5153": 36, "62529": 33, "4897": 31, "8529": 42, "113": 2, "54145": 1,
                              "64049": 28, "51457": 7, "12305": 36, "1905": 35, "4417": 2, "63297": 9, "12097": 30,
                              "11601": 16, "2177": 16, "57121": 19, "1393": 27, "913": 15, "4481": 18, "58641": 2,
                              "54545": 28, "305": 25, "1937": 4, "4113": 41, "10785": 52, "5121": 3, "60929": 2,
                              "60737": 3, "51057": 16, "11073": 22, "849": 64, "9793": 16, "12033": 7, "7425": 134,
                              "50977": 1, "53841": 25, "3489": 3, "1841": 23, "51585": 7, "2929": 23, "59169": 24,
                              "16641": 25, "54097": 6, "6161": 53, "48401": 2, "10257": 71, "3217": 15, "18753": 14,
                              "55313": 55, "13121": 2, "2817": 411, "1329": 2, "56849": 1, "3073": 45, "4609": 7,
                              "32065": 1, "1025": 6, "47873": 8, "7169": 153, "62273": 19, "3377": 33, "1185": 4,
                              "1953": 16, "16417": 40, "52609": 12, "60241": 1, "2353": 1, "59985": 1, "52993": 1,
                              "46353": 1, "52513": 3, "46609": 2, "6145": 20, "7937": 143, "2433": 34, "4369": 58,
                              "47617": 4, "4241": 2, "5649": 51, "60177": 28, "12369": 19, "13345": 140, "5633": 17,
                              "8273": 4, "6945": 51, "12113": 28, "14417": 8, "13585": 9, "49": 63, "61953": 25,
                              "4929": 121, "1569": 47, "17217": 15, "1441": 3, "57169": 1, "1297": 61, "63553": 71,
                              "4097": 33, "2721": 31, "5169": 65, "52769": 3, "63809": 5, "52561": 28, "7233": 37,
                              "9217": 94, "13825": 46, "21249": 14, "9809": 9, "54865": 1, "8993": 38, "6465": 89,
                              "15377": 69, "16913": 29, "8481": 25, "57425": 1, "2321": 142, "9473": 33, "4993": 22,
                              "7745": 2}}, "nickname": "Nick", "logout_at": 1648900059}}}
        return response

    @staticmethod
    def mock_response_vehicles_data(account_id: str):
        response = {"status": "ok", "meta": {"count": 1}, "data": {
            account_id: [{"statistics": {"wins": 454, "battles": 921}, "mark_of_mastery": 4, "tank_id": 8993},
                         {"statistics": {"wins": 1, "battles": 1}, "mark_of_mastery": 1, "tank_id": 54865}]}}
        return response

    @staticmethod
    def mock_tankopedia_achievements():
        response = {
            "status": "ok",
            "meta": {"count": 388},
            "data": {
                "crucialShotMedal": {
                    "name": "crucialShotMedal",
                    "outdated": False,
                    "section": "special",
                    "section_order": 1,
                    "image_big": "http:\/\/api.worldoftanks.eu\/static\/2.71.0\/wot\/encyclopedia\/achievement\/big\/crucialShotMedal.png",
                    "options": None,
                    "hero_info": None,
                    "name_i18n": "Crucial Shot",
                    "order": 105,
                    "type": "repeatable",
                    "image": "http:\/\/api.worldoftanks.eu\/static\/2.71.0\/wot\/encyclopedia\/achievement\/crucialShotMedal.png",
                    "condition": "• Win the battle. Newly received awards are added together. Can be obtained in Team Battles only.",
                    "description": "In 20 battles, destroy the last enemy vehicle."
                }
            }
        }
        return response

    @staticmethod
    def mock_tankopedia_badges():
        responses = {
            "status": "ok",
            "meta": {"count": 120},
            "data": {
                "1": {
                    "images": {
                        "medium_icon": "http://badge_1.png",
                        "small_icon": "http://badge_1.png",
                        "big_icon": "http://badge_1.png"
                    },
                    "badge_id": 1,
                    "name": "Gold, Beta Season",
                    "description": "Reach League I in Beta Season of the Ranked Battle mode."
                }
            }
        }
        return responses

    def tearDown(self) -> None:
        os.remove(self.db_path + '/world_of_tanks.db')
