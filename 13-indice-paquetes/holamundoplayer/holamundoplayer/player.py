"""
Este es el módulo que incluye la clase
de reproductor de música
"""


class Player:
    """
    Esta clase crear un reproductor
    de música
    """

    def play(self, song):
        """
        Reproduce la canción que recibió como parámetro

        Parameters:
        song (str): Este es un string con el path de la canción

        Returns:
        int: Devuelve 1 si reproduce con éxito, en caso de fracaso devuelve 0
        """
        print("Reproduciendo canción...")

    def stop(self):
        print("Stopping")
