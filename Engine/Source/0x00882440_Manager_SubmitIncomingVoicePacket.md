---
offset: "0x00882440"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00882440 — `Manager_SubmitIncomingVoicePacket`

- **Адрес (Offset):** `0x00882440`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00882440
void ComSat::Sound::Manager::SubmitIncomingVoicePacket(uint64_t session, uint64_t talker, uint8_t* data, uint32_t size, bool reliable) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00882440 в IDA Pro / Ghidra
