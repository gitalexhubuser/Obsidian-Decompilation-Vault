---
offset: "0x00880bb0"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00880bb0 — `Manager_Manager`

- **Адрес (Offset):** `0x00880bb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00880bb0
ComSat::Manager::Manager(ComSat::Sound::Manager& soundManager, ComSat::Network::Manager& networkManager, const ComSat::Initialization& init, ComSat::Allocator& allocator) : m_sessions(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00880bb0 в IDA Pro / Ghidra
