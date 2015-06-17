#!/usr/bin/python

import os, sys

os.chdir(os.path.dirname(__file__))

target = "../src/main/java"

files = """
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiSequenceParser.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiRepeatController.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGBeat.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGNote.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGMeasureHeader.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGString.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGTrack.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGLocalFileImporter.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGRawImporter.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGFileFormatManager.java
./TuxGuitar/src/org/herac/tuxguitar/song/factory/TGFactory.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGSong.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGFileFormatException.java
./TuxGuitar/src/org/herac/tuxguitar/song/managers/TGSongManager.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGTimeSignature.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiSequenceHandler.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/PTInputStream.java
./TuxGuitar/src/org/herac/tuxguitar/io/tg/TGInputStream.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGFileFormat.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GP1InputStream.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GP2InputStream.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GP3InputStream.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GP4InputStream.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GP5InputStream.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GTPSettings.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GTPFileFormat.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GTPFormatException.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectBend.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGNoteEffect.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGVoice.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGSongLoader.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGInputStreamBase.java
./TuxGuitar-gtp/src/org/herac/tuxguitar/io/gtp/GTPInputStream.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGDuration.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGMeasure.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGMeasureHeader.java
./TuxGuitar/src/org/herac/tuxguitar/io/tg/TGStream.java
./TuxGuitar-jsa/src/org/herac/tuxguitar/player/impl/jsa/sequencer/MidiSequencerImpl.java
./TuxGuitar-jsa/src/org/herac/tuxguitar/player/impl/jsa/utils/MidiMessageUtils.java
./TuxGuitar-jsa/src/org/herac/tuxguitar/player/impl/jsa/midiport/MidiPortProviderImpl.java
./TuxGuitar-jsa/src/org/herac/tuxguitar/player/impl/jsa/sequencer/MidiSequencerImpl.java
./TuxGuitar/src/org/herac/tuxguitar/player/impl/sequencer/MidiSequencerImpl.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiOutputPortProvider.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiSequencer.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiDevice.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiTransmitter.java
./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiReceiver.java

./TuxGuitar/src/org/herac/tuxguitar/io/tg/TGOutputStream.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGSongWriter.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGOutputStreamBase.java
./TuxGuitar/src/org/herac/tuxguitar/io/base/TGRawExporter.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGChannel.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGChord.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGColor.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGLyric.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGMarker.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGScale.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGStroke.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGTempo.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGText.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGDivisionType.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectGrace.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectHarmonic.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectTremoloBar.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectTremoloPicking.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/effects/TGEffectTrill.java
./TuxGuitar/src/org/herac/tuxguitar/song/models/TGVelocities.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTBar.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTBeat.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTDirection.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTGuitarIn.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTNote.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTSection.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTSong.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTSymbol.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTTempo.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTTrack.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTTrackInfo.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/PTSongParser.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTComponent.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTSongInfo.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTSymbol.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/base/PTPosition.java
./TuxGuitar-ptb/src/org/herac/tuxguitar/io/ptb/helper/TrackHelper.java


./TuxGuitar/src/org/herac/tuxguitar/song/managers/TGTrackManager.java
./TuxGuitar/src/org/herac/tuxguitar/song/managers/TGMeasureManager.java

./TuxGuitar/src/org/herac/tuxguitar/util/TGVersion.java

./TuxGuitar/src/org/herac/tuxguitar/player/base/MidiPlayerException.java


./TuxGuitar/src/org/herac/tuxguitar/gui/TuxGuitar.java
""".split("\n")

files = filter(lambda s: len(s) > 0, files)

for f in files:
  path = f.split('/')[3:]
  f_dest = target + '/' + '/'.join(path)
  dir_dest = os.path.dirname(f_dest)

  cmd = 'mkdir -p "%s"' % (dir_dest)
  #print cmd
  os.system(cmd)
  
  cmd = 'cp "%s" "%s"' % (f, f_dest)
  print cmd
  os.system(cmd)


