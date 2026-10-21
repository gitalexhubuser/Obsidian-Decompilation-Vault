---
offset: "0x007de5a0"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/ComSatClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007de5a0 — `VoiceSessionRosterUpdate`

- **Адрес (Offset):** `0x007de5a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/ComSatClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007de5a0
void VoiceSessionRosterUpdate(uint64_t session, uint16_t networkId, int32_t type, const char* name, const uint8_t* key, uint64_t self, uint8_t selfNetworkId, uint8_t selfFlags, int32_t count, VoiceRosterMember* members) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007de5a0 в IDA Pro / Ghidra
