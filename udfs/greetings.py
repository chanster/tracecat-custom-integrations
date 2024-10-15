from tracecat_registry import registry, RegistrySecret, secrets

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
    return {"message": "Said hello world successfully. This was added back!"}


@registry.register(
    default_title="Different Goodbye",
    display_group="Greetings",
    description="This is a function that says different goodbye",
    secrets=[test_secret],
    namespace="integrations.greetings",
)
def different_goodbye():
    return {
        "message": "Said different goodbye successfully.  Update 20.",
        "secret": secrets.get("KEY"),
    }
