---
offset: "0x00881cf0"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00881cf0 — `Manager_Manager`

- **Адрес (Offset):** `0x00881cf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00881cf0
ComSat::Sound::Manager::Manager(const ComSat::Initialization& init, ComSat::Allocator& allocator) : m_localPlayers(allocator), m_sessions(allocator), m_remoteTalkers(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00881cf0 в IDA Pro / Ghidra
