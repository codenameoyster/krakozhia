import pytest

from main import eval_answers, evals, evaluate_answers


def run_RAG(user_question: str) -> str:
    return "IDKLOL"


@pytest.mark.asyncio
async def test_run_RAG():
    generated_answers = []
    for eval in evals:
        generated_answers.append(run_RAG(eval))

    for i in range(len(evals)):
        result = await evaluate_answers(eval_answers[i], generated_answers[i])
        assert result == "PASS", f"Evaluation failed for question: {evals[i]}"
