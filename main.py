"""
ETL-Query script
"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    read_data,
)

def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "read_data",
        ],
    )
    
    args = parser.parse_args(args[:1])
    print(args.action)
    
    if args.action == "update_record":
        parser.add_argument("record_id")
        parser.add_argument("country")
        parser.add_argument("beer_sevrings")
        parser.add_argument("spirit_servings")
        parser.add_argument("wine_servings")
        parser.add_argument("total_pure_alcohol")

    if args.action == "create_record":
        parser.add_argument("country")
        parser.add_argument("beer_sevrings")
        parser.add_argument("spirit_servings")
        parser.add_argument("wine_servings")
        parser.add_argument("total_pure_alcohol")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
        
        
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
        
        
    elif args.action == "update_record":
        update_record(
            args.record_id,
            args.country,
            args.beer_sevrings,
            args.spirit_servings,
            args.wine_servings,
            args.total_pure_alcohol
        )
        
        
    elif args.action == "delete_record":
        delete_record(args.record_id)
        
        
    elif args.action == "create_record":
        create_record(
            args.country,
            args.beer_sevrings,
            args.spirit_servings,
            args.wine_servings,
            args.total_pure_alcohol
        )
        
        
    elif args.action == "read_data":
        data = read_data()
        print(data)
        
        
    else:
        print("Unknown action")


if __name__ == "__main__":
    main()

