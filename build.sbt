name := "TuxguitarParser"

version := "0.1.1"

scalaVersion := "2.11.7"

// add tuxguitar dependencies
// cf: https://groups.google.com/forum/?fromgroups=#!topic/simple-build-tool/NO8MLUrFGmg

unmanagedSourceDirectories in Compile <++= baseDirectory { base =>
  Seq(
    base / "tuxguitar-src/TuxGuitar/src",
    base / "tuxguitar-src/TuxGuitar-lib/src",    
    base / "tuxguitar-src/TuxGuitar-gm-utils/src",    
    base / "tuxguitar-src/TuxGuitar-gm-settings/src",    
    base / "tuxguitar-src/TuxGuitar-editor-utils/src",    
    base / "tuxguitar-src/TuxGuitar-midi/src",
    base / "tuxguitar-src/TuxGuitar-gtp/src",
    base / "tuxguitar-src/TuxGuitar-ptb/src",
    base / "tuxguitar-src/TuxGuitar-jsa/src",    
    base / "tuxguitar-src/TuxGuitar-gervill/src"
  )
}


