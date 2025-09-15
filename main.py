from flet import *
import json
from db import Database
from myapi import API


def main(page: Page):
    page.title = "NLP App"
    page.theme_mode = "dark"
    page.bgcolor = "BLACK"

    db = Database()
    api= API()

    def add_analysis_result(title, text):
        analyzed_column.controls.append(
            Column([
                Text(title, size=18, weight="bold"),
                Text(text, size=16)
            ], tight=True)
        )
        page.update()
        show_analyzed_results()

    def show_analyzed_results():
        page.controls.clear()
        page.add(analyzed_results)
        page.update()

    def perform_sentiment_analysis(e):
        text = sentiment_field.value
        response = api.sentiment_analysis(text)
        txt = "\n".join([f"{i['label']} -> {round(i['score'],3)}" for i in response])
        add_analysis_result("Sentiment Analysis", txt)

    def perform_emotion_analysis(e):
        text = emotion_field.value
        response = api.emotion(text)
        txt = "\n".join([f"{i['label']} -> {round(i['score'],3)}" for i in response])
        add_analysis_result("Emotion Detection", txt)

    def perform_ner(e):
        text = ner_field.value
        response = api.ner(text)
        txt = "\n".join([f"{i['word']} -> {i['entity']}" for i in response])
        add_analysis_result("Named Entity Recognition", txt)
    
    
    def perform_translation(e):
        text = translation_field.value
        translated = api.translation(text)
        # Extract translation text if it's an object or dict
        if hasattr(translated, "translation_text"):
            txt = translated.translation_text
        elif isinstance(translated, dict) and "translation_text" in translated:
            txt = translated["translation_text"]
        else:
            txt = str(translated)
        add_analysis_result("Translation", txt)

    def perform_summarization(e):
        text = text_summarization_field.value
        summary = api.text_summarization(text)
        add_analysis_result("Text Summarization", summary['summary_text'])




    def show_sentiment(e):
        page.controls.clear()
        page.add(sentiment_analysis)
        page.update()

    def show_emotion(e):
        page.controls.clear()
        page.add(emotion_detection)
        page.update()
    def show_ner(e):
        page.controls.clear()
        page.add(named_entity_recognition)
        page.update()
    def show_translation(e):
        page.controls.clear()
        page.add(translation)
        page.update()


    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def show_text_summarization(e):
        page.controls.clear()
        page.add(text_summarization)
        page.update()

    def show_homepage(e):
        page.controls.clear()
        page.add(homepage)
        page.update()

    def show_signup(e):
        page.controls.clear()
        page.add(signup)
        page.update()

    def show_login(e):
        page.controls.clear()
        page.add(login)
        page.update()

    def perform_login(e):
        email = email_field.value
        password = password_field.value

        if db.search(email, password) == 1:
            page.dialog = AlertDialog(
                modal=True,
                title=Text("Login Successful", color="BLACK"),
                content=Text("Welcome back!", color="BLACK"),
                actions=[
                    TextButton(
                        "OK",
                        on_click=lambda ev: (
                            close_dialog(ev),
                            show_homepage(ev)
                        )
                    )
                ],
                bgcolor="WHITE",
            )
            page.dialog.open = True
            page.update()
            show_homepage(e)
        else:
            page.dialog = AlertDialog(
                modal=True,
                title=Text("Login Failed", color="BLACK"),
                content=Text("Invalid email or password", color="BLACK"),
                actions=[TextButton("OK", on_click=close_dialog)],
                bgcolor="WHITE",
            )
            page.dialog.open = True
            page.update()

    def perform_signup(e):
        name = signup_name_field.value
        email = signup_email_field.value
        password = signup_password_field.value

        response = db.add_data(name, email, password)

        if response == 1:
            dlg = AlertDialog(
                modal=True,
                title=Text("Sign Up Successful", color="BLACK"),
                content=Text("You can now log in with your credentials", color="BLACK"),
                actions=[
                    TextButton(
                        "OK",
                        on_click=lambda ev: (
                            close_dialog(ev),
                            show_login(ev)
                        )
                    )
                ],
                bgcolor="WHITE",
            )
            page.dialog = dlg
            dlg.open = True
            page.update()
            show_login(e)
        else:
            dlg = AlertDialog(
                modal=True,
                title=Text("Sign Up Failed", color="BLACK"),
                content=Text("Email already exists. Please use a different email.", color="BLACK"),
                actions=[TextButton("OK", on_click=close_dialog)],
                bgcolor="WHITE",
            )
            page.dialog = dlg
            dlg.open = True
            page.update()


    email_field = TextField(
        label="Email", width=350, height=50, border_color="BLACK"
    )
    password_field = TextField(
        label="Password",
        width=350,
        height=50,
        border_color="BLACK",
        password=True,
    )

    login = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Log in to Your Account", size=16, color="BLACK"),
                email_field,
                password_field,
                ElevatedButton(
                    "Log In",
                    width=350,
                    height=50,
                    bgcolor="BLACK",
                    color="WHITE",
                    on_click=perform_login,
                ),
                Row(
                    controls=[
                        Text("Don't have an account?", color="BLACK"),
                        TextButton(
                            "Sign Up",
                            on_click=show_signup,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )

    signup_name_field = TextField(
        label="Username", width=350, height=50, border_color="BLACK"
    )
    signup_email_field = TextField(
        label="Email", width=350, height=50, border_color="BLACK"
    )
    signup_password_field = TextField(
        label="Password",
        width=350,
        height=50,
        border_color="BLACK",
        password=True,
    )

    signup = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Make a New Account", size=16, color="BLACK"),
                signup_name_field,
                signup_email_field,
                signup_password_field,
                ElevatedButton(
                    "Sign up",
                    width=350,
                    height=50,
                    bgcolor="BLACK",
                    color="WHITE",
                    on_click=perform_signup,
                ),
                Row(
                    controls=[
                        Text("Already have an Account?", color="BLACK"),
                        TextButton(
                            "Log In",
                            on_click=show_login,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )

    homepage = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Welcome Back!", size=40, color="BLACK",weight="bold"),
                Text("Choose one of the below", size=16, color="BLACK"),
                ElevatedButton("Text Summarization", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=show_text_summarization),
                ElevatedButton("Sentiment Analysis", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=show_sentiment),
                ElevatedButton("Emotion Detection", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=show_emotion),
                ElevatedButton("Named Entity Recognition", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=show_ner),
                ElevatedButton("Translation", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=show_translation),
                Row(
                    controls=[
                        Text("Want to Log out?", color="BLACK"),
                        TextButton(
                            "Log Out",
                            on_click=show_login,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )

    text_summarization_field = TextField(
        label="Input Text", width=700, height=200, border_color="BLACK", multiline=True
    )

    text_summarization = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Text Summarization", size=40, color="BLACK",weight="bold"),
                Text("Enter the text to be summarized", size=16, color="BLACK"),
                text_summarization_field,
                ElevatedButton("Summarize", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=perform_summarization),
                Text("Summary will be displayed here", size=16, color="BLACK"),
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )

    sentiment_field = TextField(
        label="Input Text", width=700, height=200, border_color="BLACK", multiline=True
    )
    sentiment_analysis = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Sentiment Analysis", size=40, color="BLACK",weight="bold"),
                Text("Enter the text to be analyzed", size=16, color="BLACK"),
                sentiment_field,
                ElevatedButton("Analyze", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=perform_sentiment_analysis),
                Text("Sentiment will be displayed here", size=16, color="BLACK"),
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )
    emotion_field = TextField(
        label="Input Text", width=700, height=200, border_color="BLACK", multiline=True
    )
    emotion_detection = Container( 
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Emotion Detection", size=40, color="BLACK",weight="bold"),
                Text("Enter the text to be analyzed", size=16, color="BLACK"),
                emotion_field,
                ElevatedButton("Detect Emotion", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=perform_emotion_analysis),
                Text("Detected emotions will be displayed here", size=16, color="BLACK"),
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )
    ner_field = TextField(
        label="Input Text", width=700, height=200, border_color="BLACK", multiline=True
    )
    named_entity_recognition = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Named Entity Recognition", size=40, color="BLACK",weight="bold"),
                Text("Enter the text to be analyzed", size=16, color="BLACK"),
                ner_field,
                ElevatedButton("Recognize Entities", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=perform_ner),
                Text("Recognized entities will be displayed here", size=16, color="BLACK"),
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )
    translation_field = TextField(
        label="Input Text", width=700, height=200, border_color="BLACK", multiline=True
    )
    translation = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            expand=True,
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Translation", size=40, color="BLACK",weight="bold"),
                Text("Enter the text to be translated", size=16, color="BLACK"),
                translation_field,
                ElevatedButton("Translate", width=350, height=50, bgcolor="BLACK", color="WHITE",on_click=perform_translation),
                Text("Translated text will be displayed here", size=16, color="BLACK"),
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )


    
    analyzed_column = Column(
        spacing=10,
        scroll="auto",
        height=600,  # Scrollable area for results
    )

    analyzed_results = Container(
        width=1500,
        height=1000,
        bgcolor="WHITE",
        border_radius=10,
        padding=20,
        content=Column(
            controls=[
                Text("NLP APP", size=30, weight="bold", color="BLACK"),
                Text("Analysis Results", size=40, color="BLACK", weight="bold"),
                analyzed_column,
                Row(
                    controls=[
                        Text("Go back to Homepage?", color="BLACK"),
                        TextButton(
                            "Homepage",
                            on_click=show_homepage,
                            style=ButtonStyle(
                                color={"": "BLUE"},
                                text_style={"": TextStyle(decoration="underline")},
                            ),
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
    )

    page.add(login)


app(target=main)
