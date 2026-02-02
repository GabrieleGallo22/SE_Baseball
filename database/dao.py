from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def get_all_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
        SELECT DISTINCT year
        FROM team
        WHERE year > 1980
        ORDER BY year
        """
        cursor.execute(query)

        for row in cursor:
            result.append((row["year"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_teams(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT DISTINCT t.name,  t.team_code, SUM(s.salary) as salary
        FROM team t
        JOIN salary s ON s.team_code = t.team_code AND s.year = t.year
        WHERE t.year = %s
        GROUP BY t.team_code, t.name
        ORDER BY t.team_code, t.name
        """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(( row["team_code"],  row["name"], row["salary"],))

        cursor.close()
        conn.close()
        return result


if __name__ == '__main__':
    DAO = DAO()
    print(DAO.get_teams(2000))