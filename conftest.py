import pytest

# This runs before every test - it slows down browser actions
# so we can visually watch each step (typing, clicking, navigating)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1000,  # pause 1000 milliseconds (1 second) between each action
    }