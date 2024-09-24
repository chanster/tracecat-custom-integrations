from tracecat_registry import registry, RegistrySecret

test_secret = RegistrySecret(name="test_secret", keys=["KEY"])


@registry.register(
    default_title="Say Hello World",
    display_group="Greetings",
    description="This is a function that says hello world",
    secrets=[test_secret],
    namespace="integrations.greetings",
)
def say_hello_world():
    print("Hello World")
    return {"message": "Said hello world successfully"}


@registry.register(
    default_title="Say Goodbye",
    display_group="Greetings",
    description="This is a function that says goodbye",
    secrets=[test_secret],
    namespace="integrations.greetings",
)
def say_goodbye():
    print("Goodbye")
    return {"message": "Said goodbye successfully"}
