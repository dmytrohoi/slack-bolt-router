from os import getenv

from slack_bolt.app.app import App

from slack_bolt_router import Router, Routers, RouteTypes


SLACK_BOT_TOKEN = getenv("SLACK_BOT_TOKEN")

app = App(token=SLACK_BOT_TOKEN)


router = Router()

# =====================================================
# Adding routers:
# Decorator usage
@router.register(type=RouteTypes.ACTION)
def generate_slots_btn(ack):
    ack()
    print("test")

# OR
# Direct adding of handler function with params
def generate_slots_btn(ack):
    ack()
    print("test")

router.add(generate_slots_btn, type=RouteTypes.ACTION)

# =====================================================
# Applying routes to Application:
# Applying of single router
router.apply_to(app)

# OR
# Applying all initialized routers
Routers.apply_to(app)

# OR
# Pass specific routers to Routers class and apply
Routers([router]).apply_to(app)

# =====================================================

app.start()
