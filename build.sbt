name := "TuxguitarParser"

version := "0.1.0"

scalaVersion := "2.11.7"

// add tuxguitar dependencies
// cf: https://groups.google.com/forum/?fromgroups=#!topic/simple-build-tool/NO8MLUrFGmg

unmanagedSourceDirectories in Compile <++= baseDirectory { base =>
  Seq(
    base / "tuxguitar-src-1.2/TuxGuitar/src",
    base / "tuxguitar-src-1.2/TuxGuitar-midi/src",
    base / "tuxguitar-src-1.2/TuxGuitar-gtp/src",
    base / "tuxguitar-src-1.2/TuxGuitar-ptb/src",
    base / "tuxguitar-src-1.2/TuxGuitar-jsa/src",    
    base / "tuxguitar-src-1.2/TuxGuitar-gervill/src"
  )
}


