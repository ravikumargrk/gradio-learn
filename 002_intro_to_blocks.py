import gradio as gr
with gr.Blocks() as app:
    txt = gr.Textbox(label="Write a note")
    out = gr.Textbox(label="Preview")
    btn = gr.Button("Preview")
    def preview(note):
        return note
    btn.click(preview, inputs=txt, outputs=out)
app.launch()