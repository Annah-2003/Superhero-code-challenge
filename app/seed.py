from models import Power, Hero, HeroPower
from flask import Flask
from app import app, db
import random


def seed_data():
    with app.app_context():
        print("🦸‍♀️ Seeding powers...")
        powers_data = [
            {"name": "super strength", "description": "gives the wielder super-human strengths"},
            {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
            {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
            {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
        ]

        for power in powers_data:
            new_power = Power(**power)
            db.session.add(new_power)

        db.session.commit()

        print("🦸‍♀️ Seeding heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]

        for hero in heroes_data:
            new_hero = Hero(**hero)
            db.session.add(new_hero)

        db.session.commit()

        print("🦸‍♀️ Adding powers to heroes...")

        strengths = ["Strong", "Weak", "Average"]
        heroes = Hero.query.all()

        for hero in heroes:
            for _ in range(random.randint(1, 3)):
                # get a random power
                power = Power.query.order_by(db.func.random()).first()

                # Use create method on the HeroPower model
                new_hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
                db.session.add(new_hero_power)

        db.session.commit()

        print("🦸‍♀️ Seeding complete!")
if __name__ == "__main__":
    seed_data()