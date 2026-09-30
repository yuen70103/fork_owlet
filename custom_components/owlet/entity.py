"""Base class for Owlet entities."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER
from .coordinator import OwletCoordinator


class OwletBaseEntity(CoordinatorEntity[OwletCoordinator], Entity):
    """Base class for Owlet Sock entities."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: OwletCoordinator,
    ) -> None:
        """Initialize the base entity."""
        super().__init__(coordinator)
        self.coordinator = coordinator
        self.sock = coordinator.sock

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info of the device."""
        connections = {("mac", self.sock.mac)} if self.sock.mac else set()
        return DeviceInfo(
            identifiers={(DOMAIN, self.sock.serial)},
            name=f"Owlet Sock {self.sock.serial}",
            connections=connections,
            suggested_area="Nursery",
            configuration_url="https://my.owletcare.com/",
            manufacturer=MANUFACTURER,
            model=self.sock.model or None,
            sw_version=self.sock.sw_version or None,
        )
