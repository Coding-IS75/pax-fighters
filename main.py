namespace SpriteKind {
    export const NPC = SpriteKind.create()
    export const Teleport = SpriteKind.create()
    export const Silverstein = SpriteKind.create()
    export const SSA2H = SpriteKind.create()
    export const MCA = SpriteKind.create()
    export const SSA1H = SpriteKind.create()
}
statusbars.onStatusReached(StatusBarKind.EnemyHealth, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Fixed, 1, function (status) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.NPC)
    sprites.destroyAllSpritesOfKind(SpriteKind.SSA2H)
    sprites.destroyAllSpritesOfKind(SpriteKind.MCA)
    scene.setBackgroundImage()
    sprites.destroyAllSpritesOfKind(SpriteKind.Silverstein)
    FIGHT = 0
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumpcount == 1) {
        MC.vy = -50
    }
    if (jumpcount == 2) {
        if (Jump < 1) {
            pauseUntil(() => Jump == 0)
            MC.vy = -75
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC, function (sprite, otherSprite) {
    MC.setPosition(0, 120)
    SS.setPosition(160, 120)
    pause(1000)
})
statusbars.onStatusReached(StatusBarKind.EnemyHealth, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Fixed, 25, function (status) {
    FIGHT = 13
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SSA2H, function (sprite, otherSprite) {
    MC_Health.value += -10
    sprites.destroyAllSpritesOfKind(SpriteKind.SSA2H)
    MC.vy = 250
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (FIGHT >= 10) {
        MCA1 = sprites.createProjectileFromSprite(assets.image`MCA1`, MC, 75, 0)
        MCA1.setKind(SpriteKind.MCA)
        MCA1.setBounceOnWall(true)
        MCA1.setVelocity(50, 0)
    }
    pause(2000)
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    MC.vy = 0
})
/**
 * Game Start
 */
sprites.onOverlap(SpriteKind.Player, SpriteKind.Teleport, function (sprite, otherSprite) {
    sprites.destroy(TP)
    scene.setBackgroundImage(assets.image`Hallway`)
    pause(2000)
    scene.cameraFollowSprite(MC)
    story.startCutscene(function () {
        story.printText("Hey! I'm Mr. Barone, your principal here at Pax", 80, 0)
        story.printText("I heard about your middle school transcript...", 80, 0)
        story.printText("High school is different, I hope you don't make the same mistake", 80, 0)
    })
    pause(16000)
    sprites.destroy(MC)
    pause(5000)
    MC.setVelocity(50, 50)
    scene.cameraFollowSprite(MC)
    MC = sprites.create(assets.image`Main Character`, SpriteKind.Player)
    MC.setPosition(80, 109)
    MC.setStayInScreen(true)
    jumpcount = 2
    scene.setBackgroundImage(assets.image`Fight 1`)
    FIGHT = 10
    MC_Health = statusbars.create(60, 7, StatusBarKind.Health)
    MC_Health.setPosition(30, 7)
    MC_Health.value = 100
    SSH = statusbars.create(60, 7, StatusBarKind.EnemyHealth)
    SSH.setPosition(130, 7)
    SSH.value = 100
    SS = sprites.create(assets.image`Silverstein`, SpriteKind.NPC)
    SS.setPosition(157, 113)
    SS.setBounceOnWall(true)
    SS.setStayInScreen(true)
    MC.ay = 250
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    MC.vx = -50
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    MC.vx = 0
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    MC.vx = 0
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    MC.vx = 50
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    if (jumpcount == 1) {
        MC.vy = 0
    }
    if (jumpcount == 2) {
        Jump += 1
    }
})
statusbars.onStatusReached(StatusBarKind.EnemyHealth, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Fixed, 75, function (status) {
    FIGHT = 11
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    MC.vy = 50
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SSA1H, function (sprite, otherSprite) {
    MC_Health.value += -5
    sprites.destroyAllSpritesOfKind(SpriteKind.SSA1H)
    MC.vy = 250
})
sprites.onOverlap(SpriteKind.NPC, SpriteKind.MCA, function (sprite, otherSprite) {
    SSH.value += -5
    sprites.destroyAllSpritesOfKind(SpriteKind.MCA)
})
statusbars.onStatusReached(StatusBarKind.EnemyHealth, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Fixed, 50, function (status) {
    FIGHT = 12
})
statusbars.onStatusReached(StatusBarKind.Health, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Fixed, 1, function (status) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.NPC)
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
    scene.setBackgroundImage()
    sprites.destroyAllSpritesOfKind(SpriteKind.Silverstein)
    FIGHT = 0
})
let SSA3: Sprite = null
let SSA2: Sprite = null
let SSH: StatusBarSprite = null
let MCA1: Sprite = null
let MC_Health: StatusBarSprite = null
let SS: Sprite = null
let TP: Sprite = null
let MC: Sprite = null
let FIGHT = 0
let jumpcount = 0
let Jump = 0
Jump = 0
jumpcount = 1
FIGHT = 0
scene.setBackgroundImage(assets.image`School`)
MC = sprites.create(assets.image`Main Character`, SpriteKind.Player)
MC.setPosition(80, 109)
MC.setStayInScreen(true)
TP = sprites.create(assets.image`myImage`, SpriteKind.Teleport)
TP.setPosition(78, 9)
tiles.setCurrentTilemap(tilemap`level2`)
scene.cameraFollowSprite(MC)
game.onUpdateInterval(5000, function () {
    if (FIGHT >= 11) {
        SSA2 = sprites.createProjectileFromSprite(assets.image`myImage1`, SS, -100, 0)
        SSA2.setKind(SpriteKind.SSA2H)
    }
})
game.onUpdateInterval(9000, function () {
    if (FIGHT >= 12) {
        SSA3 = sprites.createProjectileFromSprite(assets.image`SSA1`, SS, -75, 0)
        SSA3.setKind(SpriteKind.SSA1H)
        SSA3.setBounceOnWall(true)
        SS.setVelocity(randint(-50, 50), 0)
    }
})
game.onUpdateInterval(2000, function () {
    if (FIGHT >= 10) {
        SSA3 = sprites.createProjectileFromSprite(assets.image`SSA1`, SS, -75, 0)
        SSA3.setKind(SpriteKind.SSA1H)
        SSA3.setBounceOnWall(true)
        SS.setVelocity(randint(-50, 50), 0)
    }
})
forever(function () {
    if (MC.y >= 100) {
        pause(500)
        Jump = 0
    }
})
