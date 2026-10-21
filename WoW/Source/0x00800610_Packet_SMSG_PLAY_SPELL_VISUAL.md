---
offset: "0x00800610"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00800610 — `Packet_SMSG_PLAY_SPELL_VISUAL`

- **Адрес (Offset):** `0x00800610`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00800610
int32_t Packet_SMSG_PLAY_SPELL_VISUAL(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00800610 в IDA Pro / Ghidra
