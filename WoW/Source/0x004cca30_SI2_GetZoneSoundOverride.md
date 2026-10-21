---
offset: "0x004cca30"
module: "WoW/Source"
file: "WoW/Source/SoundInterface/SoundInterface2Internal.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004cca30 — `SI2_GetZoneSoundOverride`

- **Адрес (Offset):** `0x004cca30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/SoundInterface/SoundInterface2Internal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004cca30
int32_t SI2::GetZoneSoundOverride(int32_t mapId, int32_t chunkX, int32_t chunkY, int32_t subchunkX, int32_t subchunkY, int32_t* zoneIntroMusicId, int32_t* zoneMusicId, int32_t* soundAmbienceId, int32_t* soundProviderPreferencesId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004cca30 в IDA Pro / Ghidra
