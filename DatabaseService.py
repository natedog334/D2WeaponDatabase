from typing import Tuple
import psycopg2
import os
from enum import Enum

class SortBy(Enum):
    NAME = 0
    ARTIST = 1
    GENRE = 2
    RELEASE_YEAR = 3


# noinspection PyMethodMayBeStatic
class DatabaseService(object):

    def sample_query(self, name):
        receipt = ("""
            SELECT name FROM  MPH_TEST 
            WHERE name ='{name}'
        """.format(name=name))
        print(receipt)
        return exec_fetchall(receipt)

    def get_weapon_by_name(self, name):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where lower(guns.gun_name) like lower('{name}%')
                """)
        return exec_fetchall(receipt)

    def get_weapon_by_type(self, type):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where wt.weapon_type_name = '{type}'
                """)
        return exec_fetchall(receipt)

    def get_weapon_by_element(self, element):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where e.gun_element like '%{element}%'
                    order by wt.weapon_type_name
                """)
        return exec_fetchall(receipt)

    def get_all_primaries(self):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where e.gun_element in ('Kinetic', 'Stasis')
                    and wt.weapon_type_name not in ('grenade_launcher')
                        """)
        return exec_fetchall(receipt)

    def get_all_secondaries(self):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where e.gun_element in ('Void', 'Solar', 'Arc')
                    and wt.weapon_type_name not in ('rocket_launcher', 'grenade_launcher', 'lfr', 'machine_gun', 'sword')
                        """)
        return exec_fetchall(receipt)

    def get_all_heavies(self):
        receipt = (f"""
                    select guns.gun_name, wt.weapon_type_name, a.gun_archetype, rof.gun_rof, e.gun_element, r.gun_rarity, s.gun_source
                    from guns
                    inner join archetype a on a.archetype_id = guns.archetype_id
                    inner join element e on e.element_id = guns.element_id
                    inner join rarity r on r.rarity_id = guns.rarity_id
                    inner join rof on rof.rof_id = guns.rof_id
                    inner join source s on s.source_id = guns.source_id
                    inner join weapon_type wt on wt.weapon_type_id = guns.weapon_type_id
                    where e.gun_element in ('Void', 'Solar', 'Arc')
                    and wt.weapon_type_name in ('rocket_launcher', 'grenade_launcher', 'lfr', 'machine_gun', 'sword')
                        """)
        return exec_fetchall(receipt)

def exec_fetchone(query: str):
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        row = cur.fetchone()
        conn.close()
        return row
    except Exception as e:
        print(f"Connection failed: {e}")
        return False


def exec_fetchall(query: str):
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Connection failed: {e}")
    return False


def exec_status(query: str) -> bool:
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        try:
            conn.commit()
            conn.close()
            return True
        except:
            print("commit error")
            conn.close()
            return False
    except Exception as e:
        print(f"Exception: {e}")
    return False