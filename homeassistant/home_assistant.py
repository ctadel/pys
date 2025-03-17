#!/bin/python3

import os
import requests
import argparse

HA_TOKEN = os.environ.get('HA_TOKEN')
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZTUzMzZiNGQ5OGE0M2I5YWY4M2I1MDY3M2EzOTVlZCIsImlhdCI6MTczNzExNTU2OCwiZXhwIjoyMDUyNDc1NTY4fQ.5XQFT0_z68xGhHTOVspMJghFKk5U5x_bK2Z_mqkpVIw"

class ArgsHandler:
    def __init__(self):
        user_name = os.environ['USER']
        self.parser = argparse.ArgumentParser(description="Control Home Assistant entities")
        self.parser.add_argument(
            '--area', type=str, default=user_name, help="Area to control entities in (default: 'OS user')"
        )
        self.parser.add_argument(
            'entity', type=str, help="Entity type to control (e.g., 'lights', 'fans')"
        )
        self.parser.add_argument(
            'action', type=str, nargs='?', choices=['on', 'off', 'toggle'],
            help="Action to perform on the entity (e.g., 'on', 'off', 'toggle')"
        )

    def parse_args(self):
        return self.parser.parse_args()

    def get_entity_and_action(self):
        args = self.parse_args()
        entity = args.entity
        action = args.action.lower() if args.action else 'toggle'
        area = args.area.lower()
        return entity, action, area


class HomeAssistantController:
    def __init__(self, base_url="http://localhost:8123", token=None):
        self.base_url = base_url
        self.token = token

    def _get_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def list_entities(self, entities=None):
        url = f"{self.base_url}/api/states"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Error fetching entities: {e}")

    def control_entity_state(self, entity_id, state_action):
        if state_action not in ['on', 'off', 'toggle']:
            raise ValueError("Invalid state_action. Must be 'on', 'off', or 'toggle'.")

        domain = entity_id.split('.')[0]

        if state_action == 'toggle':
            url = f"{self.base_url}/api/services/{domain}/toggle"
        else:
            url = f"{self.base_url}/api/services/{domain}/turn_{state_action}"

        payload = {"entity_id": entity_id}

        try:
            response = requests.post(url, headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Error controlling entity: {e}")

    def control_area_entities(self, area, entity_type, action):
        domain = entity_type.rstrip('s')  # Remove plural for the domain (e.g., 'lights' -> 'light')
        if action in ('on', 'off'):
            action = "turn_" + action

        url = f"{self.base_url}/api/services/{domain}/{action}"
        payload = {"area_id": area}

        try:
            response = requests.post(url, headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def is_on(self, entity_id):
        url = f"{self.base_url}/api/states/{entity_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return False if response.json()['state'] == 'off' else True
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Error fetching entities: {e}")

if __name__ == "__main__":
    ha = HomeAssistantController(token=HA_TOKEN)
    args_handler = ArgsHandler()
    entity, action, area = args_handler.get_entity_and_action()

    if '.' in entity:
        ha.control_entity_state(entity_id=entity, state_action=action)

    else:
        ha.control_area_entities(area=area, entity_type=entity, action=action)
