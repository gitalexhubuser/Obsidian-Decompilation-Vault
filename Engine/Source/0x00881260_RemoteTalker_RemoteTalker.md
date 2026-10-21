---
offset: "0x00881260"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00881260 — `RemoteTalker_RemoteTalker`

- **Адрес (Offset):** `0x00881260`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00881260
ComSat::Sound::Manager::RemoteTalker::RemoteTalker(ComSat::Allocator& allocator) : m_allocator(&allocator), m_packets(nullptr), m_frameTime(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00881260 в IDA Pro / Ghidra
