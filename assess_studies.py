# import os
# import typer
# import json
# from dotenv import load_dotenv
# from pathlib import Path
# from typing import List
# from llm_data_extractor.providers import Antropic

# # TODO add to toml during installation

# app = typer.Typer()

# def assess_single_study(anthropic: Antropic, template: str, example: str, text: str) -> dict:
#     task = construct_prompt(template, example, text)
#     return anthropic.get_dict(task)

# def assess_multiple_studies(
#     anthropic: Antropic,
#     template: str,
#     example: str,
#     text_files: List[Path],
#     output_dir: Path
# ) -> None:
#     for text_file in text_files:
#         text = read_pdf(text_file)
#         result = assess_single_study(anthropic, template, example, text)
        
#         output_file = output_dir / f"{text_file.stem}_assessment.json"
#         with open(output_file, 'w') as file:
#             json.dump(result, file, indent=2)
        
#         typer.echo(f"Assessment completed for {text_file.name}. Results saved to {output_file}")

# @app.command()
# def main(
#     template_file: Path = typer.Option(..., help="Path to the template JSON file"),
#     example_file: Path = typer.Option(..., help="Path to the example JSON file"),
#     text_files: List[Path] = typer.Argument(..., help="Paths to the text files containing the studies to assess"),
#     output_dir: Path = typer.Option(..., help="Directory to save the output JSON files"),
#     model_name: str = typer.Option("claude-3-sonnet-20240229", help="Anthropic model name")
# ):
#     # Load environment variables
#     load_dotenv()
#     api_key = os.getenv("ANTHROPIC_API_KEY")
#     if not api_key:
#         typer.echo("Error: ANTHROPIC_API_KEY not found in environment variables", err=True)
#         raise typer.Exit(code=1)

#     # Read template and example files
#     template = read_json(template_file)
#     example = read_json(example_file)

#     # Initialize Anthropic client
#     anthropic = Antropic(api_key=api_key, model_name=model_name)

#     # Create output directory if it doesn't exist
#     output_dir.mkdir(parents=True, exist_ok=True)

#     # Assess multiple studies
#     assess_multiple_studies(anthropic, template, example, text_files, output_dir)

# if __name__ == "__main__":
#     app()