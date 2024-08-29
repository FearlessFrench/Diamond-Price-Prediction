import gradio as gr
import joblib
import numpy as np
import pandas as pd

# Load the model and unique values
model = joblib.load('model.joblib')

# Define the Gradio interface function
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })
    prediction = model.predict(input_data)[0]
    return f"Predicted Price: ${prediction:.2f}"

# Create the Gradio interface using Blocks
with gr.Blocks() as demo:
    gr.Markdown("## Diamond Price Prediction")
    with gr.Row():
        carat = gr.Number(label='Carat')
        cut = gr.Dropdown(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], label='Cut')
        color = gr.Dropdown(['D', 'E', 'F', 'G', 'H', 'I', 'J'], label='Color')
    with gr.Row():
        clarity = gr.Dropdown(['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'], label='Clarity')
        depth = gr.Number(label='Depth')
        table = gr.Number(label='Table')
    with gr.Row():
        x = gr.Number(label='x')
        y = gr.Number(label='y')
        z = gr.Number(label='z')
    
    btn = gr.Button("Predict")
    output = gr.Textbox(label='Predicted Price')

    btn.click(predict_price, inputs=[carat, cut, color, clarity, depth, table, x, y, z], outputs=output)

demo.launch()