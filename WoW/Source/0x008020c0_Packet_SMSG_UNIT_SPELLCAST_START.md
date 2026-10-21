---
offset: "0x008020c0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008020c0 — `Packet_SMSG_UNIT_SPELLCAST_START`

- **Адрес (Offset):** `0x008020c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008020c0
int32_t Packet_SMSG_UNIT_SPELLCAST_START(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008020c0 в IDA Pro / Ghidra
