import customtkinter as ctk  # Importation de la bibliothèque CustomTkinter pour l'interface graphique

# Fonction de réponse du chatbot
def chatBot_response(user_input):
    # Dictionnaire contenant les réponses prédéfinies du chatbot
    response = {
        "bonjour": "Bonjour ! Comment puis-je vous aider ?",
        "quelle heure est-il ?": "Je ne puis répondre, mais il est temps de coder !",
        "au revoir": "Au revoir ! Passez une excellente journée !",
    }
    # Retourne la réponse correspondante ou un message par défaut si la question n'est pas reconnue
    return response.get(user_input.lower(), "Désolé, je ne comprends pas la question.")

# Fonction pour gérer l'envoi du message
def send_message(event=None):
    # Récupère le message saisi par l'utilisateur
    user_message = user_input.get()
    if user_message.strip() != "":  # Vérifie que le message n'est pas vide
        # Active la zone d'affichage pour y insérer du texte
        chat_history.configure(state="normal")
        # Ajoute le message de l'utilisateur dans l'historique
        chat_history.insert('end', f"Vous: {user_message}\n", "user")
        # Génère la réponse du chatbot
        bot_response = chatBot_response(user_message)
        # Ajoute la réponse du chatbot dans l'historique
        chat_history.insert('end', f"Bot: {bot_response}\n", "bot")
        # Désactive la zone d'affichage pour empêcher l'édition
        chat_history.configure(state="disabled")
        # Fait défiler automatiquement jusqu'à la fin de l'historique
        chat_history.see("end")
        # Efface le champ de saisie de l'utilisateur
        user_input.delete(0, "end")

# Configuration de l'interface graphique
app = ctk.CTk()  # Création de la fenêtre principale
app.geometry("500x600")  # Définition de la taille de la fenêtre
app.title('Chatbot CodeGeekPro')  # Titre de la fenêtre

# Création d'une en-tête pour le chatbot
header = ctk.CTkLabel(app, text="Bienvenue sur le chatbot de codeGeekPro", font=('Arial', 18, "bold"))
header.pack(pady=10)  # Ajout d'un espace vertical autour de l'en-tête

# Zone d'affichage pour l'historique des messages
chat_history = ctk.CTkTextbox(app, height=400, state="disabled")  # Zone non modifiable
chat_history.tag_config("user", foreground="blue")  # Style pour les messages de l'utilisateur
chat_history.tag_config("bot", foreground="green")  # Style pour les messages du bot
chat_history.pack(pady=10, padx=10, fill="both", expand=True)  # Placement dans la fenêtre

# Champ de saisie pour l'utilisateur
user_input_frame = ctk.CTkFrame(app)  # Cadre pour organiser le champ de saisie et le bouton
user_input_frame.pack(pady=10, padx=10, fill="x")  # Placement dans la fenêtre

user_input = ctk.CTkEntry(user_input_frame, placeholder_text="Entrez votre message ici ....", width=350)
user_input.pack(side="left")  # Placement à gauche dans le cadre

send_button = ctk.CTkButton(user_input_frame, text="Envoyer", command=send_message)  # Bouton pour envoyer le message
send_button.pack(side="left")  # Placement à gauche dans le cadre

# Associer la touche "Entrée" au champ de saisie pour envoyer le message
app.bind("<Return>", send_message)

# Lancement de la boucle principale de l'application
app.mainloop()