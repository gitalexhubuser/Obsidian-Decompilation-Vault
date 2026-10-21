---
offset: "0x00785d60"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Snow.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00785d60 — `Snow_UpdatePacket`

- **Адрес (Offset):** `0x00785d60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Snow.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00785d60
void Snow::UpdatePacket(Packet<SnowFlakeParticleBuffer>* packet, float count, const C3Vector* origin, const C3Vector* wind) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00785d60 в IDA Pro / Ghidra
