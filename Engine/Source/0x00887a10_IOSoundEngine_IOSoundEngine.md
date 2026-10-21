---
offset: "0x00887a10"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundIOSoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00887a10 — `IOSoundEngine_IOSoundEngine`

- **Адрес (Offset):** `0x00887a10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundIOSoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00887a10
ComSat::Sound::IOSoundEngine::IOSoundEngine(const ComSat::Initialization& init, ComSat::Sound::IOCallback& callback, ComSat::Allocator& allocator) : m_allocator(&allocator), m_callback(&callback), m_captureChannel(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00887a10 в IDA Pro / Ghidra
