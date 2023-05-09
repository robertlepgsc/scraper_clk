import pytest

@pytest.fixture
def primary_data_box_content():
    box = """
    <div class="xboxcontent">
        <h1 class="color_a" id="CouncilFileHeader" style="height:32px;"><font class="cfheader">Council File: 10-0180</font><span style="margin-left:230px;"><a onclick="TagToTip('EmailSubscribe', OFFSETX, -200, ABOVE, true, CLOSEBTN, true, FOLLOWMOUSE, false, FADEIN, 700, SHADOW, true, TITLE, 'Subscribe Via Email', TITLEBGCOLOR, '#5089BE', WIDTH, 250, CLOSEBTNCOLORS, ['#CCCCCC', '#000000', '#CCCCCC', '#000000'])"><img src="/lacityclerkconnect/images/email.gif" border="0" alt="Subscribe via email" title="Subscribe via email" style="cursor:pointer"></a></span><span style="margin-left:30px;"><a target="_blank" href="index.cfm?fa=vcfi.dsp_CFMS_Report&amp;rptid=99&amp;cfnumber=10-0180"><img src="/lacityclerkconnect/images/PrintIcon.gif" border="0" width="32" height="32" alt="Print this record" title="Print this record" style="cursor:pointer"></a></span><span style="margin-left:30px;"><a target="_blank" href="https://cityclerk.lacity.org/publiccomment/?cfnumber=10-0180"><img src="/lacityclerkconnect/images/publiccomment.gif" border="0" width="32" height="32" alt="Public Comment" title="Submit a Public Comment" style="cursor:pointer"></a></span></h1>
        <div id="xboxholder" style="height:482px; position:relative;">
            <!-- change height here for overall height of box -->
            <div id="viewrecord">
                <div class="section">
                    <div class="reclabel">Title</div>
                    <div class="rectext">4800 Block of Oak Park Avenue / Plan Amendment and Zone Change</div>
                </div>
                <div class="section">
                    <div class="left">
                    <div class="reclabel">Date Received / Introduced</div>
                    <div class="rectext">01/29/2010</div>
                    </div>
                    <div class="right">
                    <div class="reclabel"></div>
                    <div class="rectext"></div>
                    </div>
                </div>
                <div class="section">
                    <div class="left">
                    <div class="reclabel">Last Changed Date</div>
                    <div class="rectext">07/09/2012</div>
                    </div>
                    <div class="right">
                    <div class="reclabel">Expiration Date</div>
                    <div class="rectext">02/01/2012</div>
                    </div>
                </div>
                <div class="section">
                    <div class="reclabel">Council District</div>
                    <div class="rectext">
                    5
                    </div>
                </div>
                <div class="section">
                    <div class="left">
                    <div class="reclabel">Mover</div>
                    <div class="rectext">
                        <div> PAUL KORETZ</div>
                    </div>
                    </div>
                    <div class="right">
                    <div class="reclabel">Second</div>
                    <div class="rectext">
                        <div> DENNIS ZINE</div>
                    </div>
                    </div>
                </div>
                <div class="section">
                    <div class="reclabel">File Activities</div>
                    <div class="rectext rowcolor1">
                    <table id="inscrolltbl" width="100%">
                        <tbody>
                            <tr>
                                <th class="ViewRecordHistory">Date</th>
                                <th class="ViewRecordHistory">Activity</th>
                                <th class="ViewRecordHistory">&nbsp;</th>
                            </tr>
                            <tr class="rowcolor3">
                                <td class="ViewRecordHistory">07/09/2012</td>
                                <td class="ViewRecordHistory">
                                File expired per Council policy, Council file No. 05-0553.
                                </td>
                                <td class="ViewRecordHistory">
                                <img alt="Click to view online docs" src="/lacityclerkconnect/images/pdficon.JPG" border="0" height="15" width="15" style="cursor:pointer" onclick="TagToTip('showtip_1', OFFSETX, -200, ABOVE, true, CLOSEBTN, true, FOLLOWMOUSE, false, FADEIN, 700, SHADOW, true, TITLE, 'Select Online Document', TITLEBGCOLOR, '#5089BE', WIDTH, 250, CLOSEBTNCOLORS, ['#CCCCCC', '#000000', '#CCCCCC', '#000000'])">
                                </td>
                            </tr>
                            <tr class="rowcolor2">
                                <td class="ViewRecordHistory">01/29/2010</td>
                                <td class="ViewRecordHistory">
                                Motion referred to Planning and Land Use Management Committee.
                                </td>
                                <td class="ViewRecordHistory">
                                <img alt="Click to view online docs" src="/lacityclerkconnect/images/pdficon.JPG" border="0" height="15" width="15" style="cursor:pointer" onclick="TagToTip('showtip_2', OFFSETX, -200, ABOVE, true, CLOSEBTN, true, FOLLOWMOUSE, false, FADEIN, 700, SHADOW, true, TITLE, 'Select Online Document', TITLEBGCOLOR, '#5089BE', WIDTH, 250, CLOSEBTNCOLORS, ['#CCCCCC', '#000000', '#CCCCCC', '#000000'])">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                <div style="visibility:hidden; display:none;">
                    <div id="showtip_1" style="display: none;">
                    <div style="width:250px;">
                        <table id="inscrolltbl" width="100%">
                            <tbody>
                                <tr height="20px">
                                <td width="75%" style="border-bottom:solid 1px #000"><a href="https://clkrep.lacity.org/onlinedocs/2010/10-0180_ca_7-9-2012.pdf" target="_blank" title="Click to view this document. File Size: 10 KB">Council Action</a></td>
                                <td width="25%" style="border-bottom:solid 1px #000">07/09/2012</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    </div>
                    <div id="showtip_2" style="display: none;">
                    <div style="width:250px;">
                        <table id="inscrolltbl" width="100%">
                            <tbody>
                                <tr height="20px">
                                <td width="75%" style="border-bottom:solid 1px #000"><a href="https://clkrep.lacity.org/onlinedocs/2010/10-0180_mot_1-29-10.pdf" target="_blank" title="Click to view this document. File Size: 50 KB">Motion</a></td>
                                <td width="25%" style="border-bottom:solid 1px #000">01/29/2010</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

    return box