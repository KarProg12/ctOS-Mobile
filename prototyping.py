import termuxgui as tg
import sys

with tg.Connection() as conn:
    activity = tg.Activity(conn)
    layout = tg.LinearLayout(activity)
    
    # 1. Elementy interfejsu
    text_title = tg.TextView(activity, "[ ctOS Mobile v1.0 ]", layout)
    text_status = tg.TextView(activity, "Status: Oczekiwanie na komende...", layout)
    
    # Dodajemy pole do wpisywania tekstu
    input_field = tg.EditText(activity, "", layout)
    
    # Przycisk zatwierdzający
    button = tg.Button(activity, "WYKONAJ PROTOKÓŁ", layout)
    
    # 2. Główna pętla obsługi zdarzeń
    for event in conn.events():
        # Sprawdzamy, czy użytkownik kliknął nasz przycisk
        if event.type == tg.Event.click and event.value["id"] == button.id:
            # Pobieramy to, co wpisałeś w pole tekstowe
            wpisany_tekst = input_field.gettext()
            
            # Jeśli wpiszesz "exit" - zamykamy aplikację
            if wpisany_tekst.strip().lower() == "exit":
                activity.finish()
                sys.exit()
            
            # W innym wypadku zmieniamy status na ekranie na Twój tekst
            text_status.settext(f"Uruchomiono: {wpisany_tekst}")
            
        # Bezpieczne wyjście z basha, jeśli zamkniesz okno gestem wstecz
        if event.type == tg.Event.destroy and event.value["finishing"]:
            sys.exit()

