import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime

Base = declarative_base()


class PlayerPersonalDataDetailsModel(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'player_personal_details'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_battle_time = Column(Integer)
    account_id = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    gold = Column(Integer)
    free_xp = Column(Integer)
    ban_time = Column(Integer)
    is_bound_to_phone = Column(Integer)
    is_premium = Column(Boolean)
    credits = Column(Integer)
    premium_expires_at = Column(Integer)
    bonds = Column(Integer)
    battle_life_time = Column(Integer)
    global_rating = Column(Integer)
    clan_id = Column(Integer)


class PlayerPersonalDataStatisticsModel(Base):
    """
    Create data model for player personal statistics data.
    """
    __tablename__ = 'player_personal_statistics'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    statistic_type = Column(String)
    spotted = Column(Integer)
    battles_on_stunning_vehicles = Column(Integer)
    avg_damage_blocked = Column(Float)
    direct_hits_received = Column(Integer)
    explosion_hits = Column(Integer)
    piercings_received = Column(Integer)
    piercings = Column(Integer)
    max_damage_tank_id = Column(String)
    max_xp_tank_id = Column(String)
    max_frags = Column(Integer)
    xp = Column(Integer)
    survived_battles = Column(Integer)
    dropped_capture_points = Column(Integer)
    hits_received = Column(Integer)
    hits_percents = Column(Integer)
    max_damage = Column(Integer)
    draws = Column(Integer)
    battles = Column(Integer)
    damage_received = Column(Integer)
    avg_damage_assisted = Column(Float)
    avg_damage_assisted_track = Column(Float)
    frags = Column(Integer)
    stun_number = Column(Integer)
    avg_damage_assisted_radio = Column(Float)
    capture_points = Column(Integer)
    stun_assisted_damage = Column(Integer)
    hits = Column(Integer)
    battle_avg_xp = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    damage_dealt = Column(Integer)
    no_damage_direct_hits_received = Column(Integer)
    shots = Column(Integer)
    explosion_hits_received = Column(Integer)
    tanking_factor = Column(Integer)
    max_frags_tank_id = Column(Integer)


class PlayerPersonalVehiclesModel(Base):
    """
    Create data model for the personal vehicles statistics.
    """
    __tablename__ = 'player_vehicles'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    tank_id = Column(String)
    battles = Column(Integer)
    mark_of_mastery = Column(Integer)


class PlayerAchievementsModel(Base):
    """
    Create data model for the achievements statistics.
    """
    __tablename__ = 'player_achievements'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    medal_type = Column(String)
    medal_name = Column(String)
    medal_quantity = Column(Integer)


class TankopediaVehiclesModel(Base):
    """
    Create data model for the tankopedia vehicles.
    """
    __tablename__ = 'tankopedia_vehicles'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    tank_id = Column(String)
    is_wheeled = Column(Boolean)
    is_premium = Column(Boolean)
    tag = Column(String)
    small_icon = Column(String)
    contour_icon = Column(String)
    big_icon = Column(String)
    type = Column(String)
    description = Column(String)
    short_name = Column(String)
    name = Column(String)
    nation = Column(String)
    tier = Column(Integer)
    price_gold = Column(Integer)
    price_credit = Column(Integer)
    is_gift = Column(Boolean)


class TankopediaAchievementsModel(Base):
    """
    Create data model for the tankopedia achievements.
    """
    __tablename__ = 'tankopedia_achievements'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String)
    outdated = Column(Boolean)
    section = Column(String)
    section_order = Column(Integer)
    image_big = Column(String)
    options = Column(String)
    hero_info = Column(String)
    name_i18n = Column(String)
    order = Column(Integer)
    type = Column(String)
    image = Column(String)
    condition = Column(String)
    description = Column(String)


class TankopediaInfoModel(Base):
    """
    Create data model for the tankopedia info.
    """
    __tablename__ = 'tankopedia_information'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    metric = Column(String)
    group = Column(String)
    alias = Column(String)
    value = Column(String)


class TankopediaMapsModel(Base):
    """
    Create data model for the tankopedia maps.
    """
    __tablename__ = 'tankopedia_maps'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String)
    camouflage_type = Column(String)
    description = Column(String)
    arena_id = Column(String)


class VehiclesStatisticsModel(Base):
    """
    Create data model for the vehicles statistics.
    """
    __tablename__ = 'vehicle_statistics'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    battle_type = Column(String)
    spotted = Column(Integer)
    battles_on_stunning_vehicles = Column(Integer)
    max_xp = Column(Integer)
    xp = Column(Integer)
    survived_battles = Column(Integer)
    dropped_capture_points = Column(Integer)
    hits_percents = Column(Integer)
    draws = Column(Integer)
    battles = Column(Integer)
    damage_received = Column(Integer)
    frags = Column(Integer)
    stun_number = Column(Integer)
    capture_points = Column(Integer)
    stun_assisted_damage = Column(Integer)
    max_damage = Column(Integer)
    hits = Column(Integer)
    battle_avg_xp = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    damage_dealt = Column(Integer)
    max_frags = Column(Integer)
    shots = Column(Integer)
    direct_hits_received = Column(Integer)
    explosion_hits = Column(Integer)
    piercings_received = Column(Integer)
    piercings = Column(Integer)
    no_damage_direct_hits_received = Column(Integer)
    explosion_hits_received = Column(Integer)
    tanking_factor = Column(Integer)
    avg_damage_blocked = Column(Integer)
    mark_of_mastery = Column(Integer)
    in_garage = Column(Boolean)
    tank_id = Column(String)


class VehiclesFragsModel(Base):
    """
    Create data model for the vehicles statistics.
    """
    __tablename__ = 'vehicle_frags'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    tank_id = Column(String)
    opponent_tank_id = Column(String)
    frags = Column(Integer)


class VehiclesAchievementsModel(Base):
    """
    Create data model for the vehicles frags.
    """
    __tablename__ = 'vehicle_achievements'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    tank_id = Column(String)
    achievement_type = Column(String)
    achievement = Column(String)
    quantity = Column(Integer)


class TankopediaBadgesModel(Base):
    """
    Create data model for the vehicles frags.
    """
    __tablename__ = 'tankopedia_badges'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    badge_id = Column(Integer)
    name = Column(String)
    medium_icon = Column(String)
    small_icon = Column(String)
    big_icon = Column(String)
    description = Column(String)


class DataModel:

    @staticmethod
    def create_tables(engine):
        Base.metadata.create_all(engine)

