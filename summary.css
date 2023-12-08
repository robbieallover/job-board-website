/// <summary>
/// Represents a CSS condition rule.
/// </summary>
abstract class CssConditionRule : CssGroupingRule, ICssConditionRule
{
    #region Fields

    readonly MediaList _media;

    #endregion

    #region ctor

    internal CssConditionRule(CssRuleType type, String conditionText, CssParser parser)
        : base(type, conditionText, parser)
    {
        _media = MediaList.Create(conditionText);
    }

    #endregion

    #region Properties

    public IMediaList Media
    {
        get { return _media; }
    }

    #endregion

    #region Methods

    protected override void ReplaceWith(ICssRule rule)
    {
        var newRule = rule as CssConditionRule;
        _media.MediaText = newRule._media.MediaText;
        base.ReplaceWith(rule);
    }

    #endregion
}
