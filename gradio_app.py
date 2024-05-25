import os

from pathlib import Path

import gradio as gr

import asyncio

import pandas as pd
from asyncflows import AsyncFlows


with gr.Blocks() as demo:
    db_url = gr.Textbox("sqlite:///dummy.db", label="Database URL", placeholder="sqlite:///dummy.db")
    query = gr.Textbox(label="Query")
    submit_button = gr.Button("Submit")
    schema_text = gr.Textbox(label="Database Schema", interactive=False)
    sql_query = gr.Textbox(label="Write a SQL Query", interactive=False)
    exec_result = gr.DataFrame(None, label="SQL Execution Result", interactive=False)
    default_output = gr.Textbox(label="Answer", interactive=False)


    async def handle_submit(database_url, query):
        # Clear the output fields
        yield {
            schema_text: "",
            sql_query: "",
            exec_result: pd.DataFrame(),
            default_output: "",
        }

        # Load the chatbot flow
        flow = AsyncFlows.from_file("sql_rag.yaml").set_vars(
            query=query,
            database_url=database_url,
        )

        # Show the database schema
        yield {
            schema_text: await flow.run("get_db_schema.schema_text")
        }

        # Show the sql query
        async for partial_results in flow.stream("generate_sql_statement.result"):
            yield {
                sql_query: partial_results
            }

        # Run the SQL query
        data = {
            "data": await flow.run("exec.data"),
            "headers": await flow.run("exec.headers"),
        }
        yield {
            exec_result: data,
        }

        # Run the question answering
        async for partial_results in flow.stream("answer_user_query.result"):
            yield {
                default_output: partial_results
            }


    submit_button.click(
        fn=handle_submit,
        inputs=[db_url, query],
        outputs=[schema_text, exec_result, default_output, sql_query]
    )


if __name__ == "__main__":
    demo.launch()
