from database.DB_connect import DBConnect
from dataclasses import dataclass

@dataclass (frozen=True)
class Team:
    id: int
    team_code: str
    name: str
    total_salary: int

class DAO:
    @staticmethod
    def get_all_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
        SELECT DISTINCT T.year
        FROM team T
        WHERE T.year>1980
        ORDER BY T.year DESC
        """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_team_of_year(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
        SELECT t.id, t.team_code, t.name, COALESCE(SUM(s.salary)) as total_salary
        FROM team t
        LEFT JOIN salary s ON s.team_code = t.team_code AND s.year = t.year
        WHERE t.year = %s
        GROUP BY t.id, t.team_code, t.name

        """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result
