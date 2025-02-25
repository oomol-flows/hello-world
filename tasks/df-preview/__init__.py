#region generated meta
import typing
class Inputs(typing.TypedDict):
  df: typing.Any
Outputs = typing.Any
#endregion

from oocana import Context

def main(params: Inputs, context: Context) -> Outputs:
    df = params["df"]

  # your code
    context.preview(df)
