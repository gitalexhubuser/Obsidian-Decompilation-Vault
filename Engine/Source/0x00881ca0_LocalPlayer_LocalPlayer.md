---
offset: "0x00881ca0"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00881ca0 — `LocalPlayer_LocalPlayer`

- **Адрес (Offset):** `0x00881ca0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00881ca0
ComSat::Sound::Manager::LocalPlayer::LocalPlayer(ComSat::Allocator& allocator) : m_sessionPriorities(allocator), m_mutedSessions(allocator), m_mutedTalkers(allocator), m_talkerVolumes(allocator), m_sessionVolumes(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00881ca0 в IDA Pro / Ghidra
