import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Checkbox(label="Morning?"),
        gr.Slider(0, 100, label="Temperature (F)")
    ],
    outputs=[
        gr.Textbox(label="Greeting"),
        gr.Number(label="Temperature (degC)")
    ]
)

if __name__ == "__main__":
    demo.launch(debug=True) # reload for development 

