
from models.clubs import Club
from models.competitions import Competitions
from models.game_lineups import GameLineup
from models.games import Games
from models.player import Player
from models.player_bio import PlayerBio
from models.player_attributes import PlayerAttributes
from models.player_photo import PlayerPhoto
import psycopg2 as dbapi2

class Database:
    def __init__(self,db_url):
         self.db_url = db_url

def get_competition(self, competition_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    competition_code,
                    name,
                    sub_type,
                    type,
                    country_id,
                    country_name,
                    domestic_league_code,
                    confederation,
                    url
                FROM
                    competitions
                WHERE
                    competition_id = %s;
            """
            cursor.execute(query, (competition_id,))
            if cursor.rowcount == 0:
                return None
            (
                competition_code,
                name,
                sub_type,
                type,
                country_id,
                country_name,
                domestic_league_code,
                confederation,
                url
            ) = cursor.fetchone()

        competition = Competitions(
            competition_id,
            competition_code,
            name,
            sub_type,
            type,
            country_id,
            country_name,
            domestic_league_code,
            confederation,
            url
        )
        return competition

def get_game_lineup(self, game_lineup_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    game_id,
                    club_id,
                    type,
                    number,
                    player_id,
                    player_name,
                    team_captain,
                    position
                FROM
                    game_lineups
                WHERE
                    game_lineup_id = %s;
            """
            cursor.execute(query, (game_lineup_id,))
            if cursor.rowcount == 0:
                return None
            (
                game_id,
                club_id,
                type,
                number,
                player_id,
                player_name,
                team_captain,
                position
            ) = cursor.fetchone()

    game_lineup = GameLineup(
        game_lineup_id,
        game_id,
        club_id,
        type,
        number,
        player_id,
        player_name,
        team_captain,
        position
    )
    return game_lineup
def get_game(self, game_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    competition_id,
                    season,
                    round,
                    date,
                    home_club_id,
                    away_club_id,
                    home_club_goals,
                    away_club_goals,
                    home_club_position,
                    away_club_position,
                    home_club_manager_name,
                    away_club_manager_name,
                    stadium,
                    attendance,
                    referee,
                    url,
                    home_club_formation,
                    away_club_formation,
                    home_club_name,
                    away_club_name,
                    aggregate,
                    competition_type
                FROM
                    games
                WHERE
                    game_id = %s;
            """
            cursor.execute(query, (game_id,))
            if cursor.rowcount == 0:
                return None
            (
                competition_id,
                season,
                round,
                date,
                home_club_id,
                away_club_id,
                home_club_goals,
                away_club_goals,
                home_club_position,
                away_club_position,
                home_club_manager_name,
                away_club_manager_name,
                stadium,
                attendance,
                referee,
                url,
                home_club_formation,
                away_club_formation,
                home_club_name,
                away_club_name,
                aggregate,
                competition_type
            ) = cursor.fetchone()

    game = Games(
        game_id,
        competition_id,
        season,
        round,
        date,
        home_club_id,
        away_club_id,
        home_club_goals,
        away_club_goals,
        home_club_position,
        away_club_position,
        home_club_manager_name,
        away_club_manager_name,
        stadium,
        attendance,
        referee,
        url,
        home_club_formation,
        away_club_formation,
        home_club_name,
        away_club_name,
        aggregate,
        competition_type
    )
    return game

def get_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                FROM
                    player
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                first_name,
                last_name,
                name,
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        name
    )
    return player
def get_players(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                FROM
                    player
                ORDER BY id;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                first_name,
                last_name,
                name,
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        name
    )
    return player
def get_player_by_name(self, name):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    id,
                    first_name,
                    last_name,
                    name
                FROM
                    player
                WHERE
                    name = %s;
            """
            cursor.execute(query, (name,))
            if cursor.rowcount == 0:
                return None
            (
                player_id,
                first_name,
                last_name,
                player_name,
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        player_name
    )
    return player

def add_player(self, player_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO player (player_id, first_name, last_name, name)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (
                player_data['player_id'],
                player_data['first_name'],
                player_data['last_name'],
                player_data['name']
            ))
def update_player(self, player_id, updated_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                UPDATE player
                SET first_name = %s, last_name = %s, name = %s
                WHERE player_id = %s;
            """
            cursor.execute(query, (
                updated_data['first_name'],
                updated_data['last_name'],
                updated_data['name'],
                player_id
            ))
def delete_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "DELETE FROM player WHERE player_id = %s;"
            cursor.execute(query, (player_id,))
            
def update_player_atr(self, atr_key, player_atr):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = """UPDATE player_attributes
                    SET
                        sub_position = %s,
                        position = %s,
                        foot = %s,
                        height_in_cm = %s,
                        market_value_in_eur = %s,
                        highest_market_value_in_eur = %s,
                        contract_expiration_date = %s
                    WHERE
                        id = %s;"""
                cursor.execute(query, (player_atr.sub_position, player_atr.position, player_atr.foot, player_atr.height_in_cm, player_atr.market_value_in_eur,
                                       player_atr.highest_market_value_in_eur,player_atr.contract_expiration_date, atr_key))
def get_player_attributes(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    player_code,
                    sub_position,
                    position,
                    foot,
                    height_in_cm,
                    market_value_in_eur,
                    highest_market_value_in_eur,
                    contract_expiration_date
                FROM
                    player_attributes
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                player_code,
                sub_position,
                position,
                foot,
                height_in_cm,
                market_value_in_eur,
                highest_market_value_in_eur,
                contract_expiration_date
            ) = cursor.fetchone()

    player_attributes = PlayerAttributes(
        player_id,
        player_code,
        sub_position,
        position,
        foot,
        height_in_cm,
        market_value_in_eur,
        highest_market_value_in_eur,
        contract_expiration_date
    )
    return player_attributes
def add_player_attributes(self, player_attributes_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO player_attributes (player_id, player_code, sub_position, position, foot, height_in_cm, market_value_in_eur, highest_market_value_in_eur, contract_expiration_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (
                player_attributes_data['player_id'],
                player_attributes_data['player_code'],
                player_attributes_data['sub_position'],
                player_attributes_data['position'],
                player_attributes_data['foot'],
                player_attributes_data['height_in_cm'],
                player_attributes_data['market_value_in_eur'],
                player_attributes_data['highest_market_value_in_eur'],
                player_attributes_data['contract_expiration_date']
            ))
            player_key = cursor.fetchone()[0]
    return player_key
def get_player_bio(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                    country_of_birth,
                    city_of_birth,
                    country_of_citizenship,
                    date_of_birth
                FROM
                    player_bio
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                first_name,
                last_name,
                name,
                country_of_birth,
                city_of_birth,
                country_of_citizenship,
                date_of_birth
            ) = cursor.fetchone()

    player_bio = PlayerBio(
        player_id,
        first_name,
        last_name,
        name,
        country_of_birth,
        city_of_birth,
        country_of_citizenship,
        date_of_birth
    )
    return player_bio

def get_player_photo(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    image_url,
                    url
                FROM
                    player_photo
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                image_url,
                url
            ) = cursor.fetchone()

    player_photo = PlayerPhoto(
        player_id,
        image_url,
        url
    )
    return player_photo

def get_club(self, club_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    club_code,
                    name,
                    domestic_competition_id,
                    total_market_value,
                    squad_size,
                    average_age,
                    foreigners_number,
                    foreigners_percentage,
                    national_team_players,
                    stadium_name,
                    stadium_seats,
                    net_transfer_record,
                    coach_name,
                    last_season,
                    url
                FROM
                    clubs
                WHERE
                    club_id = %s;
            """
            cursor.execute(query, (club_id,))
            if cursor.rowcount == 0:
                return None
            (
                club_code,
                name,
                domestic_competition_id,
                total_market_value,
                squad_size,
                average_age,
                foreigners_number,
                foreigners_percentage,
                national_team_players,
                stadium_name,
                stadium_seats,
                net_transfer_record,
                coach_name,
                last_season,
                url
            ) = cursor.fetchone()

    club = Club(
        club_id,
        club_code,
        name,
        domestic_competition_id,
        total_market_value,
        squad_size,
        average_age,
        foreigners_number,
        foreigners_percentage,
        national_team_players,
        stadium_name,
        stadium_seats,
        net_transfer_record,
        coach_name,
        last_season,
        url
    )
    return club

def get_clubs_by_search(self, search_word):
    clubs = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM clubs WHERE club_id::text LIKE %s OR club_code LIKE %s OR clubs.name LIKE %s ORDER BY club_id;"""
            search_word = "%" + search_word + "%"
            cursor.execute(query, (search_word, search_word, search_word,))
            if cursor.rowcount == 0:
                return None
            for club_id, club_code, name, domestic_competition_id, total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name, last_season, url in cursor:
                clubs.append((club_id, Club(club_id,club_code, name,domestic_competition_id,total_market_value,squad_size,average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name,last_season, url)))
    return clubs
def get_club_name(self, club_id):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = "SELECT name FROM club WHERE (id = %s);"
                cursor.execute(query, (club_id,))
                name = cursor.fetchone()[0]
        return name

def add_club(self, club_in):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """INSERT INTO clubs (club_id, club_code, name, domestic_competition_id)
             VALUES (%s, %s, %s, %s) RETURNING club_id"""
            cursor.execute(query, (club_in.club_id, club_in.club_code, club_in.name, club_in.domestic_competition_id))
            club_key = cursor.fetchone()[0]
    return club_key
def update_club(self, club_id, club):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = """UPDATE clubs
                SET name = %s, club_code = %s, total_market_value = %s, squad_size = %s, 
                    average_age = %s, foreigners_number = %s, foreigners_percentage = %s,
                    national_team_players = %s, stadium_name = %s, stadium_seats = %s, 
                    net_transfer_record = %s, coach_name = %s, last_season = %s, url = %s
                WHERE club_id = %s;"""
                cursor.execute(query, (club.club_name, club.club_code, club.total_market_value, club.squad_size, club.average_age,
                       club.foreigners_number, club.foreigners_percentage, club.national_team_players,
                       club.stadium_name, club.stadium_seats, club.net_transfer_record, club.coach_name,
                       club.last_season, club.url, club_id))


def delete_club(self, club_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                DELETE FROM clubs WHERE (club_id = %s)
            """
            cursor.execute(query, (club_id,))

            
