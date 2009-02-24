{
  'includes': [
    '../../build/common.gypi',
    '../../build/external_code.gypi',
  ],
  'target_defaults': {
    'defines': [
      'U_STATIC_IMPLEMENTATION',
    ],
    # TODO(mark): Looks like this is causing the "public" include directories
    # to show up twice in some targets in this file.  Fix.
    'include_dirs': [
      'public/common',
      'public/i18n',
      'source/common',
      'source/i18n',
    ],
    'msvs_disabled_warnings': [4005],
  },
  'targets': [
    {
      'target_name': 'icudata',
      'type': 'static_library',
      'sources': [
        'icudt38.dll',
         # These are hand-generated, but will do for now.  The linux
         # version is an identical copy of the (mac) icudt38l_dat.s file,
         # modulo removal of the .const pseudo-op and with no leading
         # underscore on the icudt38_dat symbol.
        'linux/icudt38l_dat.s',
        'mac/icudt38l_dat.s',
      ],
      'conditions': [
        [ 'OS == "win"', {
          'type': 'none',
          'msvs_tool_files': ['../../build/output_dll_copy.rules'],
        }, {  # else: OS != "win"
          'sources!': ['icudt38.dll'],
        }],
        [ 'OS != "linux"', {
          'sources!': ['linux/icudt38l_dat.s'],
        }],
        [ 'OS != "mac"', {
          'sources!': ['mac/icudt38l_dat.s'],
        }],
      ],
    },
    {
      'target_name': 'icui18n',
      'type': 'static_library',
      'sources': [
        'source/i18n/anytrans.cpp',
        'source/i18n/astro.cpp',
        'source/i18n/basictz.cpp',
        'source/i18n/bocsu.c',
        'source/i18n/buddhcal.cpp',
        'source/i18n/calendar.cpp',
        'source/i18n/casetrn.cpp',
        'source/i18n/chnsecal.cpp',
        'source/i18n/choicfmt.cpp',
        'source/i18n/coleitr.cpp',
        'source/i18n/coll.cpp',
        'source/i18n/cpdtrans.cpp',
        'source/i18n/csdetect.cpp',
        'source/i18n/csmatch.cpp',
        'source/i18n/csr2022.cpp',
        'source/i18n/csrecog.cpp',
        'source/i18n/csrmbcs.cpp',
        'source/i18n/csrsbcs.cpp',
        'source/i18n/csrucode.cpp',
        'source/i18n/csrutf8.cpp',
        'source/i18n/curramt.cpp',
        'source/i18n/currfmt.cpp',
        'source/i18n/currunit.cpp',
        'source/i18n/datefmt.cpp',
        'source/i18n/dcfmtsym.cpp',
        'source/i18n/decimfmt.cpp',
        'source/i18n/digitlst.cpp',
        'source/i18n/dtfmtsym.cpp',
        'source/i18n/dtptngen.cpp',
        'source/i18n/dtrule.cpp',
        'source/i18n/esctrn.cpp',
        'source/i18n/fmtable.cpp',
        'source/i18n/fmtable_cnv.cpp',
        'source/i18n/format.cpp',
        'source/i18n/funcrepl.cpp',
        'source/i18n/gregocal.cpp',
        'source/i18n/gregoimp.cpp',
        'source/i18n/hebrwcal.cpp',
        'source/i18n/indiancal.cpp',
        'source/i18n/inputext.cpp',
        'source/i18n/islamcal.cpp',
        'source/i18n/japancal.cpp',
        'source/i18n/measfmt.cpp',
        'source/i18n/measure.cpp',
        'source/i18n/msgfmt.cpp',
        'source/i18n/name2uni.cpp',
        'source/i18n/nfrs.cpp',
        'source/i18n/nfrule.cpp',
        'source/i18n/nfsubs.cpp',
        'source/i18n/nortrans.cpp',
        'source/i18n/nultrans.cpp',
        'source/i18n/numfmt.cpp',
        'source/i18n/olsontz.cpp',
        'source/i18n/persncal.cpp',
        'source/i18n/plurfmt.cpp',
        'source/i18n/plurrule.cpp',
        'source/i18n/quant.cpp',
        'source/i18n/rbnf.cpp',
        'source/i18n/rbt.cpp',
        'source/i18n/rbt_data.cpp',
        'source/i18n/rbt_pars.cpp',
        'source/i18n/rbt_rule.cpp',
        'source/i18n/rbt_set.cpp',
        'source/i18n/rbtz.cpp',
        'source/i18n/regexcmp.cpp',
        'source/i18n/regexst.cpp',
        'source/i18n/reldtfmt.cpp',
        'source/i18n/rematch.cpp',
        'source/i18n/remtrans.cpp',
        'source/i18n/repattrn.cpp',
        'source/i18n/search.cpp',
        'source/i18n/simpletz.cpp',
        'source/i18n/smpdtfmt.cpp',
        'source/i18n/sortkey.cpp',
        'source/i18n/strmatch.cpp',
        'source/i18n/strrepl.cpp',
        'source/i18n/stsearch.cpp',
        'source/i18n/taiwncal.cpp',
        'source/i18n/tblcoll.cpp',
        'source/i18n/timezone.cpp',
        'source/i18n/titletrn.cpp',
        'source/i18n/tolowtrn.cpp',
        'source/i18n/toupptrn.cpp',
        'source/i18n/translit.cpp',
        'source/i18n/transreg.cpp',
        'source/i18n/tridpars.cpp',
        'source/i18n/tzrule.cpp',
        'source/i18n/tztrans.cpp',
        'source/i18n/ucal.cpp',
        'source/i18n/ucln_in.c',
        'source/i18n/ucol.cpp',
        'source/i18n/ucol_bld.cpp',
        'source/i18n/ucol_cnt.cpp',
        'source/i18n/ucol_elm.cpp',
        'source/i18n/ucol_res.cpp',
        'source/i18n/ucol_sit.cpp',
        'source/i18n/ucol_tok.cpp',
        'source/i18n/ucol_wgt.c',
        'source/i18n/ucoleitr.cpp',
        'source/i18n/ucsdet.cpp',
        'source/i18n/ucurr.cpp',
        'source/i18n/udat.cpp',
        'source/i18n/udatpg.cpp',
        'source/i18n/ulocdata.c',
        'source/i18n/umsg.cpp',
        'source/i18n/unesctrn.cpp',
        'source/i18n/uni2name.cpp',
        'source/i18n/unum.cpp',
        'source/i18n/uregex.cpp',
        'source/i18n/uregexc.cpp',
        'source/i18n/usearch.cpp',
        'source/i18n/utmscale.c',
        'source/i18n/utrans.cpp',
        'source/i18n/vtzone.cpp',
        'source/i18n/windtfmt.cpp',
        'source/i18n/winnmfmt.cpp',
      ],
      'defines': [
        'U_I18N_IMPLEMENTATION',
      ],
      'dependencies': [
        'icuuc',
      ],
      'direct_dependent_settings': {
        # Use prepend (+) because the WebKit build needs to pick up these
        # ICU headers instead of the ones in ../WebKit/JavaScriptCore/wtf,
        # also in WebKit's include path.
        # TODO(mark): The double + is a bug.  It should be a single +.  It
        # seems that a + is being chopped off when the "target" section is
        # merged into "target_defaults".
        'include_dirs++': [
          'public/i18n',
        ],
      },
    },
    {
      'target_name': 'icuuc',
      'type': 'static_library',
      'sources': [
        'source/common/bmpset.cpp',
        'source/common/brkeng.cpp',
        'source/common/brkiter.cpp',
        'source/common/caniter.cpp',
        'source/common/chariter.cpp',
        'source/common/cmemory.c',
        'source/common/cstring.c',
        'source/common/cwchar.c',
        'source/common/dictbe.cpp',
        'source/common/locbased.cpp',
        'source/common/locid.cpp',
        'source/common/locmap.c',
        'source/common/locutil.cpp',
        'source/common/normlzr.cpp',
        'source/common/parsepos.cpp',
        'source/common/propname.cpp',
        'source/common/punycode.c',
        'source/common/putil.c',
        'source/common/rbbi.cpp',
        'source/common/rbbidata.cpp',
        'source/common/rbbinode.cpp',
        'source/common/rbbirb.cpp',
        'source/common/rbbiscan.cpp',
        'source/common/rbbisetb.cpp',
        'source/common/rbbistbl.cpp',
        'source/common/rbbitblb.cpp',
        'source/common/resbund.cpp',
        'source/common/resbund_cnv.cpp',
        'source/common/ruleiter.cpp',
        'source/common/schriter.cpp',
        'source/common/serv.cpp',
        'source/common/servlk.cpp',
        'source/common/servlkf.cpp',
        'source/common/servls.cpp',
        'source/common/servnotf.cpp',
        'source/common/servrbf.cpp',
        'source/common/servslkf.cpp',
        'source/common/triedict.cpp',
        'source/common/uarrsort.c',
        'source/common/ubidi.c',
        'source/common/ubidi_props.c',
        'source/common/ubidiln.c',
        'source/common/ubidiwrt.c',
        'source/common/ubrk.cpp',
        'source/common/ucase.c',
        'source/common/ucasemap.c',
        'source/common/ucat.c',
        'source/common/uchar.c',
        'source/common/uchriter.cpp',
        'source/common/ucln_cmn.c',
        'source/common/ucmndata.c',
        'source/common/ucnv.c',
        'source/common/ucnv2022.c',
        'source/common/ucnv_bld.c',
        'source/common/ucnv_cb.c',
        'source/common/ucnv_cnv.c',
        'source/common/ucnv_err.c',
        'source/common/ucnv_ext.c',
        'source/common/ucnv_io.c',
        'source/common/ucnv_lmb.c',
        'source/common/ucnv_set.c',
        'source/common/ucnv_u16.c',
        'source/common/ucnv_u32.c',
        'source/common/ucnv_u7.c',
        'source/common/ucnv_u8.c',
        'source/common/ucnvbocu.c',
        'source/common/ucnvdisp.c',
        'source/common/ucnvhz.c',
        'source/common/ucnvisci.c',
        'source/common/ucnvlat1.c',
        'source/common/ucnvmbcs.c',
        'source/common/ucnvscsu.c',
        'source/common/ucol_swp.c',
        'source/common/udata.c',
        'source/common/udatamem.c',
        'source/common/udataswp.c',
        'source/common/uenum.c',
        'source/common/uhash.c',
        'source/common/uhash_us.cpp',
        'source/common/uidna.cpp',
        'source/common/uinit.c',
        'source/common/uinvchar.c',
        'source/common/uiter.cpp',
        'source/common/uloc.c',
        'source/common/umapfile.c',
        'source/common/umath.c',
        'source/common/umutex.c',
        'source/common/unames.c',
        'source/common/unifilt.cpp',
        'source/common/unifunct.cpp',
        'source/common/uniset.cpp',
        'source/common/uniset_props.cpp',
        'source/common/unisetspan.cpp',
        'source/common/unistr.cpp',
        'source/common/unistr_case.cpp',
        'source/common/unistr_cnv.cpp',
        'source/common/unistr_props.cpp',
        'source/common/unorm.cpp',
        'source/common/unorm_it.c',
        'source/common/unormcmp.cpp',
        'source/common/uobject.cpp',
        'source/common/uprops.c',
        'source/common/ures_cnv.c',
        'source/common/uresbund.c',
        'source/common/uresdata.c',
        'source/common/usc_impl.c',
        'source/common/uscript.c',
        'source/common/uset.cpp',
        'source/common/uset_props.cpp',
        'source/common/usetiter.cpp',
        'source/common/ushape.c',
        'source/common/usprep.cpp',
        'source/common/ustack.cpp',
        'source/common/ustr_cnv.c',
        'source/common/ustr_wcs.c',
        'source/common/ustrcase.c',
        'source/common/ustrenum.cpp',
        'source/common/ustrfmt.c',
        'source/common/ustring.c',
        'source/common/ustrtrns.c',
        'source/common/utext.cpp',
        'source/common/utf_impl.c',
        'source/common/util.cpp',
        'source/common/util_props.cpp',
        'source/common/utrace.c',
        'source/common/utrie.c',
        'source/common/utypes.c',
        'source/common/uvector.cpp',
        'source/common/uvectr32.cpp',
        'source/common/wintz.c',
      ],
      'defines': [
        'U_COMMON_IMPLEMENTATION',
      ],
      'dependencies': [
        'icudata',
      ],
      'direct_dependent_settings': {
        # Use prepend (+) because the WebKit build needs to pick up these
        # ICU headers instead of the ones in ../WebKit/JavaScriptCore/wtf,
        # also in WebKit's include path.
        # TODO(mark): The double + is a bug.  It should be a single +.  It
        # seems that a + is being chopped off when the "target" section is
        # merged into "target_defaults".
        'include_dirs++': [
          'public/common',
        ],
        'conditions': [
          # TODO(mark): Do we need this as a dependent setting on any platform?
          # If we actually do need it, it's probably Windows-only...
          [ 'OS != "mac"', {
            'defines': [
              'U_STATIC_IMPLEMENTATION',
            ],
          },],
        ],
      },
      'conditions': [
        [ 'OS == "win"', {
            'sources': [
              'source/stubdata/stubdata.c',
            ],
        },],
      ],
    },
  ],
}
