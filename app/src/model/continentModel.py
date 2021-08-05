from model.db import DB


class ContinentModel():
    def __init__(self):
        self.conn = DB.connect()

    def fetch_all_continent(self):
        self.conn.execute(
            """ SELECT * from continent
            """
        )
        rows = self.conn.fetchall()
        return rows

    def add_continent(self, data):
        self.conn.execute(
            f"""
            insert into continent(id_continent, nom_continent)values("{data.get('id')}", "{data.get('nom')}");
            """
        )

    def delete_continent(self, id):
        self.conn.execute(
            f"""
            DELETE FROM continent WHERE id_continent = {int(id)}
            """
        )

    def update_continent(self, data):
        self.conn.execute(
            f"""
            UPDATE continent SET NOM_CONTINENT = '{data.get('nom')}' WHERE ID_COnTINENT = {data.get('id')}
            """
        )
