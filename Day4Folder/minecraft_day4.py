# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def come():
    agent.teleport_to_player()


player.on_chat("come", come)

def fw(num):
    agent.move(FORWARD, num)

player.on_chat("fw", fw)


def bk(num):
    agent.move(BACK, num)

player.on_chat("bk", bk)

def ml(num):
    agent.move(LEFT, num)

player.on_chat("ml", ml)


def mr(num):
    agent.move(RIGHT, num)

player.on_chat("mr", mr)


def up(num):
    agent.move(UP, num)

player.on_chat("up", up)


def down(num):
    agent.move(DOWN, num)

player.on_chat("down", down)

def tl():
    agent.turn(LEFT)

player.on_chat("tl", tl)

def tr():
    agent.turn(RIGHT)

player.on_chat("tr", tr)

def chop(num):
    for i in range(num):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.destroy(UP)
        agent.move(UP, 1)

player.on_chat("chop", chop)

def mine(num):
    for i in range(num):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("mine", mine)

def build(height,width):
    for i in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(DOWN, 3)
        agent.move(RIGHT, 1)

player.on_chat("wall", build)

def solvespiral():
    while agent.inspect(AgentInspection.BLOCK, DOWN) != DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK, RIGHT):
            agent.turn(RIGHT)

        agent.move(FORWARD, 1)

player.on_chat("solvespiral", solvespiral)

def solvemaze():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        if not agent.detect(AgentDetection.BLOCK, LEFT):
            agent.turn(LEFT)
            agent.move(FORWARD, 1)

        elif not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)

        else:
            agent.turn(RIGHT)
            agent.move(FORWARD, 1)

player.on_chat("solvemaze", solvemaze)






