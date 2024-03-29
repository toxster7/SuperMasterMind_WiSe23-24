class MenuPrinter:

    """
    diese klassse dient dazu funktionen zu implimentieren
    die die unterschiedlichen menüs anzeigt
    1. displayMenu -> zeigt das start menu an
    2. displayRoleType -> zeigt die möglichen rolle an
    3. displayGameType -> zeigt die möglichen spielmodi

    @authro: Ilai, Berkan
    """
    def displayMenu() -> None:

        """
        diese funktion dient dazu, das start menü,
        für das spiel anzuzeigen
        """

        print(
        """
                __,                     ,__
             __/==+\      Spielmenü     /+==\__
                "  "`  ================ '"  "

            +------------------------------------+
            | Superhirn ein Logikspiel für deine |
            |           high performance!        |
            |   Bitte wähle einer der Optionen:  |
            |                                    |
            |                                    |
            |       [1] Spiel starten            |
            |       [2] Spiel beenden            |
            +------------------------------------+
        """
        )

    def displayRoleType() -> None:

        """
        diese funktion dient dazu die unterschiedlichen
        rollen für das spiel anzuzeiegn
        """

        print(
        """
            +------------------------------------+
            | Superhirn ein Logikspiel für deine |
            |           high performance!        |
            |   Bitte wähle einer der Optionen:  |
            |                                    |
            |                                    |
            |       [1] Codierer                 |
            |       [2] Rater                    |
            +------------------------------------+
        """
        )

    def displayGameType() -> None:

        """
        diese funktion dient dazu die unterschiedlichen
        spieltypen anzuzeigen, ob der nutzer lokal mit einem
        bot oder über das netzwerk mit einem bot spielen möchte
        """

        print(
        """
            +------------------------------------+
            | Superhirn ein Logikspiel für deine |
            |           high performance!        |
            |   Bitte wähle einer der Optionen:  |
            |                                    |
            |                                    |
            |       [1] Lokales Spiel            |
            |       [2] Über das Netzwerk        |
            +------------------------------------+
        """
        )

    def displayGameOptionsLocal() -> None:
        """
        diese funktion dient dazu, die möglichen spiel
        optionen, die der user festlegen kann anzuzeigen
        """

        print(
        """
            +------------------------------------+
            |   Du kannst gleich mit dem Spiel   |
            |   starten. Du muss noch ein paar   |
            |        Spieloptionen setzten       |
            |                                    |
            |                                    |
            |                                    |
            +UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU+
        """
        )
