"""Support for Owlet switches."""

from __future__ import annotations

from typing import Any

from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import OwletCoordinator
from .entity import OwletBaseEntity

SWITCHES: tuple[SwitchEntityDescription, ...] = (
    SwitchEntityDescription(
        key="base_station_on",
        translation_key="base_on",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Owlet switch based on a config entry."""
    coordinators: list[OwletCoordinator] = list(
        hass.data[DOMAIN][config_entry.entry_id].values()
    )

    switches = []
    for coordinator in coordinators:
        switches.extend(
            OwletBaseSwitch(coordinator, switch)
            for switch in SWITCHES
            if switch.key in coordinator.sock.properties
        )
    async_add_entities(switches)


class OwletBaseSwitch(OwletBaseEntity, SwitchEntity):
    """Defines a Owlet switch."""

    entity_description: SwitchEntityDescription

    def __init__(
        self,
        coordinator: OwletCoordinator,
        description: OwletSwitchEntityDescription,
    ) -> None:
        """Initialize owlet switch platform."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{self.sock.serial}-{description.key}"
        self._attr_is_on = False

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and (
            not self.sock.properties.get("charging", False)
        )

    @property
    def is_on(self) -> bool:
        """Return if switch is on or off."""
        return self.sock.properties.get(self.entity_description.key, False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on the switch."""
        await self.sock.control_base_station(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the switch."""
        await self.sock.control_base_station(False)
